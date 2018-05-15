# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:08:57 2017

@author: dixy
"""

def triFactor(n):
    """ returns the first number that has over n factors """
    """BRUTE FORCE"""
    num = 0 #the number we are checking, each time it loops through the for loop, increment 1 
    numFactor = 0
    inc = 1 #increment number
    while n>numFactor:
        num = num+ inc
        inc += 1
        numFactor = 0 #reset this number each time we loop through the factors of a number 
        for x in range(1,num+1):
            #factor loop
            if(num%x == 0):
                #print(num, " is factorized by ", x)
                numFactor += 1
        #print(num, " has ", numFactor, " factors")
        
        
    return num