# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:37:43 2017

@author: dixy
"""

def collatz(n):
    """ returns the longest sequence collatz sequence within integer n """
    """ if its even then divide by 2; if it's odd, do (3n+1)/2 """
    ans = [0,0] #keeps track largest sequence
    for x in range(n,0,-1):
        maxSeq = [x,0]
        while x != 1:
            if x%2 == 0:
                x = x/2
                maxSeq[1] += 1
            elif x%2 != 0:
                x = (3*x+1)/2
                maxSeq[1] += 2
        if maxSeq[1]>ans[1]:
            ans = maxSeq
    return ans
        
def collatzB(n):
    """ uses caching to keep track of all the previous computed paths """
    cache = [0]*n
    seqLen = 0 #length of longest sequence
    num = 0 #longest number
    for x in range(2,n):
        #current number
        seq= x #number that we are going to change following along the path
        while(seq != 1 and seq>=x):
            if seq%2 == 0:
                cache[x] += 1
                seq = seq//2
            elif seq%2 != 0:
                cache[x] += 1 
                seq = 3*seq + 1 
        cache[x] += cache[seq]
        if(cache[x]>seqLen): #change the final answer within the for loop
            seqLen = cache[x]
            num = x
    return num