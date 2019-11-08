# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:35:48 2019

@author: Félix FERRAND
"""

# function
def findDivisor(n):
    divisors = []
    
    for i in range(2, n+1):
        if n%i == 0:
            divisors.append(str(i))
            
    if len(divisors) > 2:
        message = str(n) + " a pour diviseur(s) : " + ", ".join(divisors)
    else:
        message = str(n) + " est un nombre premier"
        
    return message
            
# execution
inputInteger = int(input("Rentrez un entier strictement positif : "))

print(findDivisor(int(inputInteger)))
