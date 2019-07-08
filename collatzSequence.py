#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 23:32:10 2019

@author: janicelove
"""
import sys 

#Function to perform collatz sequence on any number selected by user
def collatz(number):
    if number  % 2 == 0:
        result = number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
    
    while result ==1:
        print (result)
        sys.exit()
    
    while result != 1:
        print (result)
        number = result
        return collatz(number)
        

print ('Pick any number:')
try:
    number = int(input())
    collatz(number)
except ValueError:
    print ('You must enter an integer type.')


