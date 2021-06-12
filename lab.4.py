# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:50:24 2021

@author: Ania
"""

ciag=[4,3,5,2,1]
n=5
maksimum=ciag[0]
imax=0
i=1


while i<n:
    if i>maksimum:
        maksimum=i
        imax=i
        i=i+1
        
        
print(maksimum)
