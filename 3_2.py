# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:34:51 2019

@author: natur
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def wave(x,y,z):
    if x>z:
        r = 0
    elif x>y:
        r = 1
    else:
        r = 0
    return r

t = np.linspace(-5,5,100)
y = np.array([wave(x,-2.5,2.5) for x in t])
f1 = np.sin(30*t+math.pi/2)*y
f2 = np.array([wave(x,0,4) for x in t])
f = np.convolve(f1,f2)
plt.plot(f)
plt.show()