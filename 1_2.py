# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 19:22:01 2019

@author: natur
"""

import numpy as np
import matplotlib.pylab as plt
import math
import matplotlib

t = np.linspace(0,10.0)
x1 = 4*np.exp(-0.5*t)*np.sin(math.pi*t + math.pi/2)
plt.title(u'4exp(-0.5t)cos(Πt)')
plt.plot(t,x1)