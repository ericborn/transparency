# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:37:33 2019

@author: Eric Born
"""
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs

# setup options to make chrome headless
opts = Options()
opts.headless = True

# loads the chromedriver exe which opens a chrome window
driver = webdriver.Chrome(r'C:/chomedriver/chromedriver.exe', options=opts)

# comment out three lines above if chrome needs to be run with a head
#driver = webdriver.Chrome(r'C:/chomedriver/chromedriver.exe')

# loads the URL
driver.get('https://c6axa542.caspio.com/dp/b5be7000b00c6c32872649618e72?rnd=1573681939421')

# finds and clicks the search button
botton = driver.find_element_by_name('searchID')
botton.submit()

# convert the page to beautiful soup format
soup = bs(driver.page_source, 'html.parser')

# selects all table data
table = soup.findAll('div', {"class": "cbResultSetPanelDataContainer"})

test_list = []

# prints text between the span elements
for span in soup.select('span'):
    test_list.append(span.text)
    #print(span.text)

# 3-43, 47-87
# last object is 1055
test_list[87]

# converts textarea to a string
text = str(soup.text)

# splits on '|type' and only keeps the last indexed item by using -1
text = text.split('<span class="cbResultSetListViewDataLabel cbResultSetNestedAlign">', 1)[-1]