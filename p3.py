# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 21:44:22 2017

@author: dixy
"""

def largestPrime(n):
    #finds the largest prime factor of n, start from top to bottom, returns itself if no prime is found
    ans = n-1
    largest = n
    while(ans>1):
        if(n%ans==0):
            check = ans-1
            while(check>=0):
                if(check == 1):
                    #if ans is only divisible by 1, ans is a prime
                    return ans
                if(ans%check == 0):
                    #if divisible break out the loop since ans is not a prime
                    break
                check = check -1 
        ans = ans-1
        print("ans is ", ans)
    return largest 

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors


pfs = prime_factors(194)
largest_prime_factor = max(pfs)