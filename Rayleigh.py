# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import scipy.optimize as sco
from scipy.optimize import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 
d = pd.read_csv("C:/Users/wiaibb5/Desktop/Book1.csv")

x = np.array(d['x'])
y = np.array(d['y'])
def model1(x,a,b):
      return a*(1 -np.exp( -1*(x/b)**2))
model = np.vectorize(model1)
 
init_guess = [0.5,0.5]
fit = curve_fit(model, d['x'],d['y'],
                p0 = init_guess,
                absolute_sigma = True)
ans, cov = fit
a, b = ans
print(a,b)

fig, ax = plt.subplots()
ax.scatter(d['x'],d['y'])

ax.plot(a*(1.0-np.exp( -1.0*(d['x']/b)**2)))