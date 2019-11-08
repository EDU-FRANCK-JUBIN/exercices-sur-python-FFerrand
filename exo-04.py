# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:54:28 2019

@author: Félix FERRAND
"""

import re

# function
def testAdn(adn):
    
    regex = re.search("[^acgt]", adn, re.IGNORECASE)
    if regex:
        return "invalide"
    else:
        return "valide"
    
# execution
inputAdn = input("Rentrez une séquence d'ADN : ")
print("la séquence est : " + testAdn(inputAdn))
