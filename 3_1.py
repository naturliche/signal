# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 21:12:23 2019

@author: natur
"""

import numpy as np
import matplotlib.pyplot as plt

def wave(x,y,z):
    if x>z:
        r = 0
    elif x>y:
        r = 1
    else:
        r = 0
    return r

x = np.linspace(-3,6,1000)
f1 = np.array([wave(t,0,1)  for t in x])
f2 = 2*x*f1
f = np.convolve(f1,f2)
plt.plot(f)
plt.show()