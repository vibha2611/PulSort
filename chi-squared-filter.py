import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chromedriver="C:\Program Files (x86)\chromedriver.exe"
browser= webdriver.Chrome(chromedriver)
browser.get('http://psrsearch.wvu.edu/psc/index.php')

#login
username = browser.find_element_by_name('username')
username.send_keys('your_username')
password = browser.find_element_by_name('password')
password.send_keys('your_password')
browser.find_element_by_name("remember").click()
browser.find_element_by_name("submit").click()

#pulsars are generally concentrated in certain parts of the sky. This code returns RA values that pass the initial filter.
start_ID=31351 #start somewhere
start_set=[]
RA=[]
Dec=[]
DM=[]
plot_number=[]
for i in range(10):  #how many datasets?
    browser.get('http://psrsearch.wvu.edu/psc/preview.php?datasetID='+str(start_ID))
    text = browser.find_element_by_tag_name("table").get_attribute("outerHTML")
    df=pd.read_html(text, header=0)
    df=df[0]
    for i in range(len(df)):
        if df['χ2'].iloc[i]>2 and df['DM (pc cm-3)'].iloc[i]>2 and df['DM (pc cm-3)'].iloc[i]<400: #for tighter filter, check galactic electron density map and alter DM accordingly
            plot_number.append(i+1)
            DM.append(df['DM (pc cm-3)'].iloc[i])
            RA.append(df["RA"].iloc[i])
            Dec.append(df["Dec"].iloc[i])
            start_set.append(start_ID)
            dict={"RA": RA, "Dec":Dec, "DM":DM, "Search ID": start_set, "Plot index": plot_number}
    start_ID=start_ID+1

df_save=pd.DataFrame(dict)
x=pd.DataFrame(df_save["RA"].value_counts())
print (x)
