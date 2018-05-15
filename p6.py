# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:47:25 2017

@author: dixy
"""

def sumDif(n):
    """ returns the difference between the sum of all natural num to n squared - summed squared individual natural number"""
    squareDif = 0
    for x in range(1,n+1):
        squareDif += x**2
    sumSquareDif = 0
    sumSquareDif = ((1+n)*(n/2))**2 #add first num to second num, and then multiply by half of size n/2
    return abs(squareDif-sumSquareDif)