# import dependencies
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import os

# open login screen
driver_path = input("Enter driver filepath: ")
chromedriver = driver_path
browser = webdriver.Chrome(chromedriver)
browser.get('http://psrsearch.wvu.edu/psc/index.php')

# login
username = browser.find_element_by_name('username')
username.send_keys('username')
password = browser.find_element_by_name('password')
password.send_keys('password')
browser.find_element_by_name("submit").click()

# inputs
search_id = int(input("Enter search ID: "))  # will not work for dataset no. 219 and below
directory = input("Enter path to download to: ")
no_datasets = int(input("How many datasets? "))
min_chi_squared = float(input("Enter minimum chi-squared value for the filter: "))
custom_dm = input("Using max. DM limit? Y/N")
if custom_dm == "Y" or custom_dm == "y":
    max_dm = float(input("Enter DM upper limit: "))
else:
    max_dm = 400

# initialise lists
links_to_check = []
reject = []

# obtaining individual plot links
counter = search_id
for i in range(no_datasets):
     browser.get('http://psrsearch.wvu.edu/psc/preview.php?datasetID='+str(counter))
     elems = browser.find_elements_by_xpath("//a[@href]")
     for elem in elems:
         link = str(elem.get_attribute("href"))
         if 'plotID' in link:
             links_to_check.append(link)
     counter = counter + 1

# marking single pulse plot links
x = 30
while x < len(links_to_check):
    for y in range(4):
        links_to_check[x + y]="spp"
    x = x + 34

# defining remove from list function
def del_from_list(name, val):
    name = [j for j in name if j != val]
    return name

links_to_check = del_from_list(links_to_check, "spp")

#rejecting DM < 2, DM out of range and low chi-squared plots
for i in range(no_datasets):
    url = 'http://psrsearch.wvu.edu/psc/preview.php?datasetID='+str(search_id)
    browser.get(url)
    text = browser.find_element_by_tag_name("table").get_attribute("outerHTML")
    df = pd.read_html(text, header = 0)
    df = df[0]
    for j in range(len(df)):
        if df['χ2'].iloc[j] > min_chi_squared and df['DM (pc cm-3)'].iloc[j]>2 and df['DM (pc cm-3)'].iloc[j] < max_dm:
            pass
        else:
            reject.append(i * 30 + j)
    search_id = search_id + 1

# marking rejected plot links
for index in reject:
    links_to_check[index] = "rejected"

# removing rejected plots from the list of links to check
links_to_check = del_from_list(links_to_check, "rejected")

filter_percent = (len(links_to_check) / (no_datasets * 30)) * 100

for link in links_to_check:
    browser.get(link)
    img = browser.find_element_by_xpath('//*[@id="plotImg"]')
    src = img.get_attribute('src')
    path = src.split('results/', 1)[1]
    path = path.replace('/', '_')
    urllib.request.urlretrieve(src, os.path.join(directory,path))

browser.close()
print(filter_percent)
