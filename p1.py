# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 21:29:32 2017

@author: dixy
"""
import math
def ans(upperlimit):
    #finds the sum of multiples of 3 and 5 until it hits the upperlimit
    sum = 0
    real = upperlimit-1
    for i in range((real//3)+1):
       # print("i is ", i)
        #we need to account for intersection (multiples of 15)
        if((i*3)%15 != 0):
            sum += i*3
    for x in range((real//5)+1):
       # print("x is ", x)
        sum += x*5
    return sum