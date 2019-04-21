# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 20:29:57 2019

@author: natur
"""

import scipy.signal as signal
import matplotlib.pyplot as plt
system = ([2,1],[1,4,3])
#t,y = signal.impulse(system) 冲激响应
t,y = signal.step(system) #阶跃响应
plt.plot(t,y)
plt.show()