# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 15:42:24 2018
@author: 李萱
"""
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
#from pprint import pprint
import requests
import concurrent 
import re
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
import os

url='https://www.etax.nat.gov.tw/etw-main/web/ETW183W1/'
html=requests.get(url).content.decode('utf-8')
sp=BeautifulSoup(html,'html.parser')

table=sp.find('table',{'class':"footable table default" })
rows=table.find_all('a',href=True,title=True)

title_array=[]
link_array=[]
for title in rows:
    title_array.append(title['title'])
    link_array.append(title['href'])

link_dict = dict(zip(title_array, link_array))
link_dict ={i:link_dict[i] for i in link_dict if len(i)==28 and link_dict[i]!='/etw-main/web/ETW183W3_10111'}    #len可以改為regex

font = FontProperties(fname=os.environ['WINDIR']+'\\Fonts\\kaiu.ttf', size=16)

def plot(cal_dict,category,mon,flag):
    plt.figure(figsize=(20,5))
    plt.bar(range(len(cal_dict)), list(cal_dict.values()), align='center')
    plt.xticks(range(len(cal_dict)), list(cal_dict.keys()),fontproperties=font, rotation=45)
    if flag == 0: plt.yticks(np.arange(0, 11, 1))
    if flag == 1: plt.yticks(np.arange(0,101,5))
    plt.title('%s年 發票得獎 %i萬 統計圖'%(mon,category),fontproperties=font)
    plt.xlabel('縣市',fontproperties=font)
    plt.ylabel('發票張數',fontproperties=font)
    plt.show()
    
sum_dict_1={'基隆市':0,'臺北市':0,'新北市':0,'桃園市':0, '新竹市':0, '新竹縣':0, '苗栗縣':0,'臺中市':0,'彰化縣':0,'南投縣':0,'雲林縣':0,'嘉義市':0,'嘉義縣':0,'臺南市':0,'高雄市':0,'屏東縣':0,'臺東縣':0,'花蓮縣':0,'宜蘭縣':0,'金門縣':0,'澎湖縣':0}
sum_dict_2={'基隆市':0,'臺北市':0,'新北市':0,'桃園市':0, '新竹市':0, '新竹縣':0, '苗栗縣':0,'臺中市':0,'彰化縣':0,'南投縣':0,'雲林縣':0,'嘉義市':0,'嘉義縣':0,'臺南市':0,'高雄市':0,'屏東縣':0,'臺東縣':0,'花蓮縣':0,'宜蘭縣':0,'金門縣':0,'澎湖縣':0}
tmp={'基隆市':0,'臺北市':0,'新北市':0,'桃園市':0, '新竹市':0, '新竹縣':0, '苗栗縣':0,'臺中市':0,'彰化縣':0,'南投縣':0,'雲林縣':0,'嘉義市':0,'嘉義縣':0,'臺南市':0,'高雄市':0,'屏東縣':0,'臺東縣':0,'花蓮縣':0,'宜蘭縣':0,'金門縣':0,'澎湖縣':0}    

def calculate(address,category,mon,cal_dict):
    for i in address:
        for state in re.findall(r'">([\u4e00-\u9fa5]{3})',str(i)):
            state = state.replace('桃園縣','桃園市')
            if category==1000:
                cal_dict[state]+=1
                sum_dict_1[state]+=1
            if category==200:
                cal_dict[state]+=1
                sum_dict_2[state]+=1          
    #plot(cal_dict,category,mon,0)    #算個月的張數
    if mon == '10305':               #指定年月份
        plot(cal_dict,category,mon,0)
    
def find_winners(sp,mon):
    add1=[]
    add2=[]
    table=mon_sp.find('tbody')
    rows=table.find_all('tr') 
    for row in rows:
        address1=row.find('td',{'headers':'companyAddress'})
        add1.append(address1)
        cal_dict_1=tmp.copy()
    calculate(add1,1000,mon,cal_dict_1)
    del add1[:]       
    
    table2=table.find_next('tbody')
    rows2=table2.find_all('tr') 
    for row2 in rows2:
        address2=row2.find('td',{'headers':'companyAddress2'})
        add2.append(address2)
        cal_dict_2=tmp.copy()
    calculate(add2,200,mon,cal_dict_2)
    del add2[:]

if __name__=="__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=35) as excutor:
        for key, value in link_dict.items() :
            mon_url='https://www.etax.nat.gov.tw'+value
            mon=re.findall(r'https://www.etax.nat.gov.tw/etw-main/web/ETW183W3_([0-9]{5})',mon_url)
            mon_html=requests.get(mon_url)
            mon_html.encoding='big-5'
            mon_sp=BeautifulSoup(mon_html.text,'html.parser')
            find_winners(mon_sp,mon[0])
            if mon[0] == '10201':
                plot(sum_dict_1,1000,'102-107',1)
                plot(sum_dict_2,200,'102-107',1)
