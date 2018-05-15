# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:53:47 2017

@author: dixy
"""

def bigint(n):
    bigint = str(2**n)
    Sum = 0
    while(len(bigint)>0):
        Sum += int(bigint[-1])
        bigint = bigint[:-1]
    return Sum
    