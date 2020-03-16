# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 23:51:32 2018

@author: 001
"""
def stackperms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in stackperms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

    
for idx, p in enumerate(stackperms([1,2,3])):
    print(idx,p)
