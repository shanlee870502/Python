# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 22:44:27 2018
@author: 李萱
"""

from bs4 import BeautifulSoup
import requests

url='https://data.gov.tw/news'
html=requests.get(url).content.decode('utf-8')
sp=BeautifulSoup(html,'html.parser')
table=sp.find('table',{'class':"table table-hover table-striped sticky-enabled"})
rows=table.find_all('tr')
for idx,row in enumerate(rows[1:]):
    date=row.find('td',{'class':'td-date'})
    title=row.find('td',{'class':'td-title'})
    print('{:4d}. {} {}'.format(idx+1,date.text,title.text))
    