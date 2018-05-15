# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 20:34:30 2018

@author: dixy
"""
def sumLetter():
    """
    returns the total sum of letters from 1-1000
    """
    one = 36 # for 1-9, no pattern 
    ten = 70 #for 10-19
    twe = 36*8 + 10*(6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) #twenty to 99
    hun = 7*9 #counting only 100,200....900
    hund = one + hun + (one + ten + twe)*9 + 10 * 891 + one*99 #why is it 891? from one-hundred
    print(hund)
    Sum = one + ten + twe + hund + 11 #from 1000
    return Sum