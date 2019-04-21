# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 13:21:06 2019

@author: natur
"""

import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    return np.array(x > 0, dtype=np.int)


X = np.arange(0, 10, 0.1)a
Y = step_function(X)
plt.plot(X, Y)
f1 = plt.ylim(-0.1, 1.1) # 指定图中绘制的y轴的范围
plt.show()