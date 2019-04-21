# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 20:21:22 2019

@author: natur
"""

import numpy as np
import matplotlib.pylab as plt
import math
import matplotlib

k = np.linspace(0,10.0,10)
x1 = 7*0.6**k*np.sin(0.9*math.pi*k+ math.pi/2)
plt.title(u'7(0.6)**k cos(0.9Πk)')
plt.stem(k,x1)