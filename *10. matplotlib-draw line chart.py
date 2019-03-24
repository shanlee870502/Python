# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 14:25:52 2018

@author: 001
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os 
def Transfer(char):
    if char=='高':
        return 100
    if char=='中':
        return 50
    else:
        return 10
    
font = FontProperties(fname=os.environ['WINDIR']+'\\Fonts\\kaiu.ttf', size=16)
data2=list()
data=np.array([['高','低','中','低','中'],['低','中','高','高','中'],['高','中','中','低','中']])

for row in data:
    data2.append(list(map(Transfer,row)))

data2=np.array(data2)
label= ['甲', '乙', '丙']
plt.figure(figsize=(10,5))
for i in range(3):
    plt.plot(np.arange(data2.shape[1]),data2[i,:],label=label[i])

plt.xticks(np.arange(data2.shape[1]),['103','104','105','106','107'],fontproperties=font)    
plt.legend(loc='低 中 高',prop=font)
plt.title('甲公司、乙公司、丙公司103年~107年業績',fontproperties=font)
plt.xlabel('年',fontproperties=font)
plt.ylabel('業績',fontproperties=font)
plt.show()
