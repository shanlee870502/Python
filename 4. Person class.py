# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 21:27:34 2018

@author: 001
"""

import datetime

class Person:
    def __init__(self,name,surname,birthdate,address,telephone,email,age):
        self.name=name
        self.surname=surname
        self.birthdate=birthdate
        self.address=address
        self.telephone=telephone
        self.email=email
        today=datetime.date.today()
        self.age=today.year-self.birthdate.year     ##why??
        
    def estimate_age(self):
        today=datetime.date.today()
        if today>datetime.date(today.year,self.birthdate.month,self.birthdate.day):
            self.age=today.year-self.birthdate.year
    @property
    def fullname(self):
        print(self.name,self.surname)
        

    
    
   

            
            
            
    
    
        
