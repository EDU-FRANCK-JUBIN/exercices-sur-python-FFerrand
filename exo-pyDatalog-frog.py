# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 10:34:41 2019

@author: Félix FERRAND
"""

from pyDatalog import pyDatalog

pyDatalog.create_terms('X');

pyDatalog.load("""    
    frog(X) <= croakes(X) & eatsFlies(X)
    canary(X) <= chirps(X) & sings(X)
    green(X) <= frog(X)
    yellow(X) <= canary(X)
    
    + croakes(fritz)
    + eatsFlies(fritz)
""")

print(pyDatalog.ask('green(X)'))
