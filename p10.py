# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 15:40:59 2017

@author: dixy
"""


def sickAlg(n):
    
    """ uses Sieve of Eratosthenes to find the sum of all primes within n """
    """METHOD:
    Create a list l of consecutive integers {2,3,…,N}.
    Select p as the first prime number in the list, p=2.
    Remove all multiples of p from the l.
    set p equal to the next integer in l which has not been removed.
    Repeat steps 3 and 4 until p2 > N, all the remaining numbers in the list are primes"""
    prime = []
    ans = 0 
    for x in range(0,n+1):
        numTuple = [x, True]
        prime.append(numTuple) #cant use tuple because tuples are not immutable 
    prime[0][1] = False #set 0 as not prime
    prime[1][1] = False #set 1 as not prime 
    nextPrime = prime[2][0]
    while nextPrime**2 <n:
        for y in range(nextPrime, n+1, nextPrime):
            #we set all multiples of nextPrime to False, and increment the for loop with nextPrime also
            prime[y][1] = False
        ans += nextPrime
        for i in range(nextPrime,n):
            #this loop looks for the nextPrime
            if prime[i][1] == True:
                nextPrime = prime[i][0]
                break
    #print(nextPrime)
    #print(ans)
    for a in range(nextPrime, n+1):
        if prime[a][1] == True:
            #print(prime[a][0])
            ans += prime[a][0]
    return ans
            
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    