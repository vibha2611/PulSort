#inputs
search_id=int(input("Enter search ID: "))  #will not work for dataset no. 219 and below
directory=input("Enter path to download complete plots to: ")
driver=input("Enter driver filepath: ")
no_datasets=int(input("How many datasets? "))
min_chi_squared=float(input("Enter minimum chi-squared value for the filter: "))
custom_dm=input("Using max. DM limit? Y/N ")

if custom_dm=="Y" or custom_dm=='y':
    max_dm=float(input("Enter DM upper limit: "))
else:
    max_dm=400
    
ps_subfolder=input("Enter path of folder into which phase-subband subplots should be downloaded: ")
pp_subfolder=input("Enter path of folder into which pulse profile subplots should be downloaded: ")

pp_model= input("Enter pulse profile model filepath: ")
ps_model= input("Enter phase-subband model filepath: ")

def download_plots(search_id, directory, no_datasets, min_chi_squared, max_dm):
    #import dependencies
    import pandas as pd
    import selenium
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import urllib
    import os

    #open login screen
    browser= webdriver.Chrome(driver)
    browser.get('http://psrsearch.wvu.edu/psc/index.php')

    #login
    username = browser.find_element_by_name('username')
    username.send_keys('<your username>')
    password = browser.find_element_by_name('password')
    password.send_keys('<your password>')
    browser.find_element_by_name("submit").click()

    #initialise lists
    links_to_check=[]
    reject=[]

    #obtaining individual plot links
    counter=search_id
    for i in range(no_datasets):
         browser.get('http://psrsearch.wvu.edu/psc/preview.php?datasetID='+str(counter))
         elems = browser.find_elements_by_xpath("//a[@href]")
         for elem in elems:
             link=str(elem.get_attribute("href"))
             if 'plotID' in link:
                 links_to_check.append(link)
         counter=counter+1        

    #marking single pulse plot links
    x=30
    while x<len(links_to_check):
        for y in range(4):
            links_to_check[x+y]="spp"
        x=x+34    

    #defining remove from list function
    def del_from_list(name, val):
        name=[j for j in name if j!=val]
        return name

    links_to_check=del_from_list(links_to_check, "spp")

    #rejecting DM<2, DM out of range and low chi-squared plots
    for i in range(no_datasets):
        url='http://psrsearch.wvu.edu/psc/preview.php?datasetID='+str(search_id)
        browser.get(url)
        text = browser.find_element_by_tag_name("table").get_attribute("outerHTML")
        df=pd.read_html(text, header=0)
        df=df[0]
        for j in range(len(df)):
            if df['χ2'].iloc[j]>min_chi_squared and df['DM (pc cm-3)'].iloc[j]>2 and df['DM (pc cm-3)'].iloc[j]<max_dm:
                pass
            else: 
                reject.append(i*30+j)
        search_id=search_id+1

    #marking rejected plot links
    for index in reject:
        links_to_check[index]="rejected"

    #removing rejected plots from the list of links to check
    links_to_check=del_from_list(links_to_check, "rejected")

    filter_percent=(len(links_to_check)/(no_datasets*30))*100

    for link in links_to_check:
        browser.get(link)
        img=browser.find_element_by_xpath('//*[@id="plotImg"]')
        src=img.get_attribute('src')
        path=src.split('results/', 1)[1]
        path=path.replace('/', '_')
        urllib.request.urlretrieve(src, os.path.join(directory,path))

    browser.close()
    print(str(filter_percent)+ " of plots were downloaded")
    print("Plot download complete...")
    return

def crop(directory, ps_subfolder, pp_subfolder):
    from PIL import Image
    import os.path, sys

    dirs = os.listdir(directory)

    for img in dirs:
        fullpath = os.path.join(directory,img)
        if os.path.isfile(fullpath):
                im = Image.open(fullpath)
                pulse_profile = im.crop((0, 0, 205, 140))
                pulse_profile_path=os.path.join(pp_subfolder, img)
                pulse_profile.save(pulse_profile_path + 'pulse profile.png', "png", quality=100)
                phase_subband = im.crop((295, 150, 505, 405))
                phase_subband_path=os.path.join(ps_subfolder, img)
                phase_subband.save(phase_subband_path + ' phase-subband.png', "png", quality=100)


    print("Cropping complete...")
    return

def predict(pp_model, ps_model, pp_subfolder, ps_subfolder):
    import cv2
    import tensorflow as tf
    import os.path, sys
    from PIL import Image
    import pandas as pd

    categories = ["Pulsar", "Not a pulsar", "RFI-Pulsar"]

    def prepare(file):
        IMG_SIZE = 210
        img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        img_array = img_array/255
        new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
        return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

    pp_model = tf.keras.models.load_model(pp_model)
    ps_model = tf.keras.models.load_model(ps_model)

    dirs=os.listdir(pp_subfolder)

    pp_predictions=[]
    ps_predictions=[]

    for item in dirs:
        image=os.path.join(pp_subfolder, item)
        image=prepare(image)
        prediction = pp_model.predict([image])
        prediction = list(prediction[0])
        pp_predictions.append(categories[prediction.index(max(prediction))])

    dirs=os.listdir(ps_subfolder)

    predictions=[]
    for item in dirs:
        image=os.path.join(ps_subfolder, item)
        image=prepare(image)
        prediction = ps_model.predict([image])
        prediction = list(prediction[0])
        ps_predictions.append(categories[prediction.index(max(prediction))])
        
    pulsar_count=0
    for i in range(len(dirs)):
        if ps_predictions[i]=="Pulsar" and (pp_predictions[i]=="Pulsar" or pp_predictions[i]=="RFI-Pulsar"):
            pulsar_count=pulsar_count+1
    print("Number of pulsars found= "+str(pulsar_count))
    return

download_plots(search_id, directory, no_datasets, min_chi_squared, max_dm)
crop(directory, ps_subfolder, pp_subfolder)
predict(pp_model, ps_model, pp_subfolder, ps_subfolder)
