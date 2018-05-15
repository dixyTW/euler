# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 22:10:50 2017

@author: dixy
"""

def evenFib(N):
    #returns the even value up to N in the Fibonacci sequence 
    first = 1 
    ans = 1
    even = 0
    for x in range(N):
        print("first is ", first)
        print("ans is ", ans)
        first += ans
        if(first>N):
            break
        if(first%2 == 0):            
            even += first
        ans += first
        if(ans>N):
            break
        if(ans%2 == 0):
            even += ans

    return even

def V2(N):
    #improved version
    first = 1
    second = 1
    track = 0
    ans = 0
    while(track<N):
        track = first + second
        if track%2 == 0:
            ans += track
        