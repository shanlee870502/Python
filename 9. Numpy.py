# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 16:08:11 2018
@author: Administrator
"""
import numpy as np
a = np.array([54, 27, 66, 77, 10,  0, 72, 74, 59])
b = np.array([52, 90, 94, 85, 53, 59, 35, 59, 86])
#1.c = a.reshape(3,3)，請問c是a的一個複製還是一個view?
c=a.reshape(3,3)
if np.may_share_memory(a,c)==True:
    print("create a view (Share memory)")
else:
    print("create a copy (Do not share a memory")
print("\n")
#2.寫出一行敘述，建立z使得a為z的第0行(z[:,0])，b為z的第1行(z[:,1])。
z=np.random.randint(1,100,(6,6))
print(z)
a=z[:,0]
print(a)
b=z[:,1]
print(b)
print("\n")
#3.寫出一行敘述，建立z使得a為z的第0列(z[0,:])，b為z的第1列(z[1,:])。
z=np.random.randint(50,200,(9,9))
print(z)
a=z[0,:]
print(a)
b=z[1,:]
print(b)
print("\n")
#4.用boolean mask完成計算b[i]比a[i]大的個數。
a = np.array([54, 27, 66, 77, 10,  0, 72, 74, 59])  #initialize
b = np.array([52, 90, 94, 85, 53, 59, 35, 59, 86])  #initialize
count=0
mask=b>a
print(mask.sum())
print("\n")
#5.用boolean mask完成將b[i]比a[i]大的元素複製到w。
w=[]
temp=np.where(mask)
for i in temp:
    w.append(b[i])
print(w)
print("\n")
#6.用boolean mask完成將b裡滿足b[i]>b[i-1]且b[i]>b[i+1]的所有元素(b[0],b[-1]排除在外)複製到w。
w=[]
for i in b:
    if i>1 and i<10:
        mask1=b[i]>b[i-1]
        mask2=b[i]>b[i+1]
        
temp=np.where(mask1 and mask2)
for i in temp:
    w.append(b[i])
print(w)
print("\n")
