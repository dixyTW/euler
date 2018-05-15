# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 22:10:28 2017

@author: dixy
"""
def largePal():
    """finds the 2 largest 3-digit multiplication that returns a palindrome"""
    num = []
    for x in range(999,99,-1):
        for y in range(999,99,-1):
            ans = x*y
            if isPal(ans):
                num.append(ans)
    return max(num)
    
def isPal(n):
    """helper function to check if a number is a palindrome or not """
    string = str(n)
    half = len(string)//2
    reverse = string[::-1]
    return string[:half]==reverse[:half]

