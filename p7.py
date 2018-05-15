# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:55:28 2017

@author: dixy
"""

def prime(n):
    """returns the nth prime number """
    counter = 2 #counts which prime number we are at 
    prime = [2] #prime number list
    current = 3 #current number 
    isPrime = False
    while(counter<=n):
        if(n == 1):
            return prime
        if(current%2 == 0):
            #if its divisble by 2, skip this number
            current += 1
        else:
            for x in range(len(prime)):
                #we use the list of primes we currently have to check if the current number is a prime
                if(current%prime[x] == 0):
                    current+=1
                    break
                if(x == len(prime)-1):
                    isPrime = True 
            #if the current number goes through all the numbers without breaking the loop, 
            #this number is prime and increment counter
            if(isPrime):
                prime.append(current)
                counter += 1 
                current += 1 #if its the last number it still increments it, causing the return value to be larger
                isPrime =False
    return current-1 #adjust for the incrementation from above
    