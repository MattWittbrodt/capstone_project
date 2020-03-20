# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:53:32 2020

@author: mattw
"""

import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
import requests


url = "https://www.yelp.com/collection/Z3iwKFIDwScWaYjcBG6v-g?utm_content=Collections&utm_source=ishare"

page = requests.get(url)
soup = BeautifulSoup(page.text, features = "lxml")


r_list = soup.findAll(class_ = 'biz-name js-analytics-click')

r2_list = []

for z in range(1,len(r_list)):
    start = str(r_list[z]).find('<span>') + 6
    end = str(r_list[z]).find('</span>')
    name = str(r_list[z])[start:(end-1)]
    print(name)
    r2_list.append(name)