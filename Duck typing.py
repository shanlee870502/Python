# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 20:10:56 2018

@author: 李萱

"""
def distance(p1,p2):
    if hasattr (p1,'x') and hasattr(p1,'y') and hasattr(p2,'x') and hasattr(p2,'y'):
        return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0.5
    else:
        raise AttributeError
class p1:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class p2:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
a=p1(3,4) 
b=p2(5,6)

C=distance(a,b)

print(C)   