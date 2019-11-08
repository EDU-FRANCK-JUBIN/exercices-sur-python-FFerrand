# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:25:12 2019

@author: Félix FERRAND
"""

import math

# function
def calculateConeVolume(radius, height):
    area = math.pi * radius ** 2
    volume = area * height / 3
    return volume

# execution
inputRadius = float(input("Rayon du cône : "))
inputHeight = float(input("Hauteur du cône : "))

print (calculateConeVolume(inputRadius, inputHeight))
