# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:30:45 2017

@author: dixy
"""
def triplet():
    for x in range(1,500):
        for y in range(x,500):
            c = 1000 - x - y
            if c**2 == x**2 + y**2:
                return c*x*y