# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 14:22:30 2018

@author: 001
"""
'''
1.下面程式若是把lock.acquire()與lock.release()那兩行刪掉，計算結果為什麼不對?

import threading
import numpy as np
def my_proc(data,lock):
    for _ in range(100000):
        lock.acquire()
        for i in range(data.size):
          data[i] = data[i] + 1
        lock.release()

lock = threading.Lock()
data = np.array([1,2,3,4])
thread1 = threading.Thread(target=my_proc,args=(data,lock))
thread2 = threading.Thread(target=my_proc,args=(data,lock))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(data)
2. 下面程式為什麼會正常?

import threading
import numpy as np
def my_proc(data):
    for _ in range(100000):
        data += 1

data = np.array([1,2,3,4])
thread1 = threading.Thread(target=my_proc,args=(data,))
thread2 = threading.Thread(target=my_proc,args=(data,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(data)
3. 下面程式為什麼會輸出[1,2,3,4]?

import threading
import numpy as np
def my_proc(data,lock):
    for _ in range(1000):
        lock.acquire()
        data = data + 1
        lock.release()

lock = threading.Lock()
data = np.array([1,2,3,4])
thread1 = threading.Thread(target=my_proc,args=(data,lock))
thread2 = threading.Thread(target=my_proc,args=(data,lock))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(data)
''

1.因為有race condition，即代表這個程式是同步的(synchronized)，在一個thread執行時，會將資料蓋掉，因而會產生出不同的結果

2.就算沒有lock也不會發生race condition，因為這個程式不是同步的(thread1做完後才會執行thread2)

3.data = data + 1 是boolean mask，並不會改變data[]裡面元素(element)的任何值，若要更改元素的值(即在for迴圈裡是有做運算的)，則變成 data[_]=data[_]+1即可。
