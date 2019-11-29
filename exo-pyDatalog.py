# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 10:34:41 2019

@author: Félix FERRAND
"""

from pyDatalog import pyDatalog
pyDatalog.create_terms('factorial, N')

factorial[N] = N*factorial[N-1]
factorial[1] = 1

print (factorial[3] == N)
