# -*- coding: utf-8 -*-
"""
Created on Sat May 15 01:21:20 2021

@author: socha
"""

x = [9,4,7,3,1]
print("dany jest ciąg:", x)

n=5

i=1
j=i+1

print("prosze uporzadkowac ciag")
for i in range (1, n-1):
    if x[0]>x[1]:
        x[1]=x[0]
        x[0]=x[1]
        
print("nowa kolejnosc ciagu", x)

