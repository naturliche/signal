# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:53:43 2019

@author: natur
"""

import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import pandas as pd
 
def wgn(x, snr):
    snr = 10**(snr/10.0)
    xpower = np.sum(x**2)/len(x)
    npower = xpower / snr
    return np.random.randn(len(x)) * np.sqrt(npower)
 
t = np.arange(0, 1000000) * 0.1
x = np.sin(t)
n = wgn(x, 6)
pl.subplot(211)
pl.hist(n, bins=100, normed=True)
pl.show()
'''
pl.subplot(212)
pl.psd(n)
'''
'''
first
x = pd.Series(n)
'''
'''
second
'''
x = plt.xcorr(n,n)
x = np.array(x)
plt.plot(t,x.autocorr)
pl.show()