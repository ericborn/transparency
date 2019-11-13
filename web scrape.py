# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:37:33 2019

@author: Eric Born
"""
import json
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs

opts = Options()
opts.set_headless()

# loads the chromedriver exe which opens a chrome window
driver = webdriver.Chrome(r'C:/chomedriver/chromedriver.exe')

# loads the URL
driver.get('https://c6axa542.caspio.com/dp/b5be7000b00c6c32872649618e72?rnd=1573681939421')

# finds and clicks the search button
botton = driver.find_element_by_name('searchID')
botton.submit()



# Pulls down the main page
#response = requests.get('https://www.10news.com/transparency-project-database-search-officer-involved-shootings-law-enforcement-misconduct-cases')
response = requests.get('https://c6axa542.caspio.com/dp/b5be7000b00c6c32872649618e72?rnd=1573681939421')


json_response = ((response.text.split))



# Decodes the page
page_src = response.content.decode('utf-8')

# convert the page to beautiful soup format
soup = bs(page_src, 'html.parser')



# Creates an empty list to store all weapon main view page links
weapLinks = []

# Store links in a list
for link in soup.find_all('a'):
    #print(link.get('href'))
    weapLinks.append(link.get('href'))