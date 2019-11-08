# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:30:30 2019

@author: Félix FERRAND
"""

import math

# function
def calculateE(n):
    e = 0
    for i in range(0, n+1):
        e += 1 / math.factorial(i)
        
    return e
        

# execution
inputInteger = int(input("Rentrez un entier supérieur à 50 : "))

e = calculateE(inputInteger)
difference = abs(math.e - e)

list = ["valeur calculée : "+ str(e), "erreur d'approximation : " + str(difference)]

print(" avec une ".join(list))
