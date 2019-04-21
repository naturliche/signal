# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 19:41:36 2019

@author: natur
"""

import numpy as np
import matplotlib.pylab as plt


def wave(x,y,z):
    if x>z:
        r = 0
    elif x>-2:
        r = 1
    else:
        r = 0
    return r
x = np.linspace(-3,6,10)
y = np.array([wave(t,-2,5) for t in x])
plt.stem(x,y)
plt.show()