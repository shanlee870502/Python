# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 20:40:42 2019

@author: 001
"""

import requests

import re

#https://data.gov.tw/news

url='https://data.gov.tw/news'

html=requests.get(url).content.decode('utf-8')

for idx,title in enumerate(re.finditer(r'<tr><td class="td-date">([0-9]{4}/[0-9]{2}/[0-9]{2})</td><td class="td-title"><a href="[^>]+?>([^<]+)',html)):

    print("{:4d}.  {}  {}".format(idx+1,title.group(1),title.group(2)))
