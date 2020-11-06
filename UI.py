# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:00:40 2020

@author: WZN3SZH
"""
import requests
pload = {'username':'Olivia','password':'123'}
r = requests.post('https://httpbin.org/post',data = pload)
print(r.text)