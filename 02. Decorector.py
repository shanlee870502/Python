# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 22:20:47 2018

@author: 001
"""
from functools import wraps
import time

def measure(func):
    @wraps(func)
    
    def _time_it(*args, **kwargs):
        a= time.time()
        try:
            return func(*args, **kwargs)
        finally:
            b= time.time() 
            print('處理程序耗時: {} 秒'.format(b-a))
    return _time_it

@measure
def f1(n=1000000):
    s = 0
    for i in range(n):
        s += i
        
f1()

@measure
def f2(n=1000000):
  s = 0
  lst = list(range(n))
  for i in lst:
      s += i
  return s

f2()
