import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chromedriver="C:\Program Files (x86)\chromedriver.exe"
browser= webdriver.Chrome(chromedriver)
browser.get('http://psrsearch.wvu.edu/psc/index.php')
#login
username = browser.find_element_by_name('username')
username.send_keys('vibha')

password = browser.find_element_by_name('password')
password.send_keys('pulsarsearch')
browser.find_element_by_name("remember").click()
browser.find_element_by_name("submit").click()

#determine optimal RA
start_ID=31351
start_set=[]
RA=[]
Dec=[]
DM=[]
plot_number=[]
for i in range(10):
    browser.get('http://psrsearch.wvu.edu/psc/preview.php?datasetID='+str(start_ID))
    text = browser.find_element_by_tag_name("table").get_attribute("outerHTML")
    df=pd.read_html(text, header=0)
    df=df[0]
    for i in range(len(df)):
        if df['χ2'].iloc[i]>2 and df['DM (pc cm-3)'].iloc[i]>2 and df['DM (pc cm-3)'].iloc[i]<400:
            plot_number.append(i+1)
            DM.append(df['DM (pc cm-3)'].iloc[i])
            RA.append(df["RA"].iloc[i])
            Dec.append(df["Dec"].iloc[i])
            start_set.append(start_ID)
            dict={"RA": RA, "Dec":Dec, "DM":DM, "Search ID": start_set, "Plot index": plot_number}
    start_ID=start_ID+1

df_save=pd.DataFrame(dict)
print(df_save)

x=pd.DataFrame(df_save["RA"].value_counts())
print (x)

#collects all values 
##allthedata = browser.find_element_by_tag_name("table").get_attribute("outerHTML")
##complete_df=pd.read_html(allthedata, header=0)
##complete_df=complete_df[0]
##for x in range(len(df_save)):
##    if 
##print(complete_df)
##
##elems = browser.find_elements_by_xpath("//a[@href]")
##first_link=[]
##for elem in elems:
##    first_link.append(str(elem.get_attribute("href")))
##
##first_link=first_link[12:-4]
##new=[]
##for i in range(len(first_link)):
##    if 'preview' in str(first_link[i]):
##        new.append(str(first_link[i]))
##print(new)
##
###scrape data
##
