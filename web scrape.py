# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:37:33 2019

@author: Eric Born
"""
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


# Pulls down the main page
page = requests.get('https://www.10news.com/transparency-project-database-search-officer-involved-shootings-law-enforcement-misconduct-cases')

'https://c6axa542.caspio.com/dp/b5be7000b00c6c32872649618e72?rnd=1573681939421'

# Decodes the page
page_src = page.content.decode('utf-8')

# convert the page to beautiful soup format
soup = bs(page_src, 'lxml')

