# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:29:32 2018

@author: 00757303 李萱
"""
import re

s1='A12345A\nBA12345\nCADA\nA'
s2='(asd)sdasd)(asdsd)asdasd)(asdas)'
s3='(1,234)5678(123)987(100,888,909)'
s4='大雄有3隻羊2條狗，小明有狗3隻雞2隻，小花有1頭牛3隻豬2隻雞狗5條。'



for m in re.finditer('A',s1):       #1.使用re.finditer('A',s1)找出每個A的位置
    print(m.start())

reg1 = re.match("A", s1)                 #2. 使用re寫出找出s1裡在每一行開頭的A
print(reg1.span() if reg1 is not None else None)

    
list_a=re.findall(r'\(.+\)',s2)         #3.比較re.findall(r'\(.+\)',s2)與re.findall(r'\(.+?\)',s2)差別
print(list_a)
list_b=re.findall(r'\(.+?\)',s2)
print(list_b)

#re+ Matches 1 or more occurrence of preceding expression.
#re? Matches 0 or 1 occurrence of preceding expression.

list_c=re.findall(r'\(.+?\)',s3)
list_c = ' '.join(list_c).replace('(','').split()    #4 計算s3裡所有()裡的整數的和
list_c = ' '.join(list_c).replace(')','').split()
list_c = ' '.join(list_c).replace(',',' ').split()
result=0

for i in list_c:
    result+=int(i)
print(result)


list_d= re.compile(r'\w+')
list_d=list_d.findall(s4)


list_sum=0
result=re.findall(r'[+-]?\d+',str(list_d))

for i in result:
    i=(int(i))
    list_sum+=i
    
print(list_sum)


