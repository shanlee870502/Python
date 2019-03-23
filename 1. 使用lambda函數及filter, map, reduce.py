# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 18:28:20 2018

@author: Shan Lee
"""
import math

a=[1,-2,3,-4,5,-6,-7,-8,9,10]

for i in filter(lambda x: x % 3 ==0,a):    #使用filter,選擇a裡正的且為3的倍數。
    print (i)


for i in map(lambda x:math.exp(-x),a):    #使用map,將a裡的元素的對映至math.exp(-a)
    print(i)

from functools import reduce               #使用reduce計算a裡的元素絕對值的和
for i in range(0,len(a)):
    a[i]=abs(a[i])
    
print(reduce(lambda x,y:x+y,a) )
