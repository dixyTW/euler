# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 14:07:23 2017

@author: dixy
"""

def div(n):
    """the function returns the smallest number that can be divisible within all numbers from 1 to n """
    """
    METHOD: we count all the unique numbers within the range of n, if a number can 
    be fromed by previous numbers in the list, dont store the number, 
    and check if its possible to multiply the smallest number
    so the number can be fromed
    eg. if we have 4 and want to form 8, we can simply multiply 2 to 
    get 8 instead of adding 8, numbers such as primes would be unique so the for loop would loop through
    all possibilities and just add the prime number
    if it can't be fromed, add the number. (prime)
    once we get all unique numbers, multiply everything within the list
    """
    ans = []
    for x in range(2,n+1):
        """the loop that counts all the divising number"""
        #n+1 because we want to include the value n+1 also
        if(n == 1):
            return 1
        elif len(ans) == 0:
            ans.append(x)
        else:
            form(ans, x)
            """check if formable by the numbers within the ans list, 
            if formable, add the appropriate number, if not formable, 
            simply add the number x """
    val = ans[0] #start from 2
    print("factor list is now ", ans)
    for i in range(1,len(ans)):
        #range(1,n) starts from 3
        #use all ints in the ans list and -1 to prevent index out of range
        val = val*ans[i]
    return val

def form(numList, k):
    """ takes in a list and check if the number k is formable by multiplying, 
    k is the number being added to the list""" 
    for y in range(len(numList)):
        if k%numList[y] == 0:
            #replace k so we can use this replaced value to go through the rest of the list
            k = k/numList[y]
            #numList.append(numList[y]) if k is divisible by numlist that means the number is already in there, therefore
            #we dont need to add it 
    numList.append(k)
    
    
    

    