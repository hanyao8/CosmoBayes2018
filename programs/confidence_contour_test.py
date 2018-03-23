# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 20:41:04 2018

@author: Choon
"""

import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#Set up the 2D Gaussian:
delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
sigma = 1.0
Z = mlab.bivariate_normal(X, Y, sigma, sigma, 0.0, 0.0)
#Get Z values for contours 1, 2, and 3 sigma away from peak:
z1 = mlab.bivariate_normal(0, 1 * sigma, sigma, sigma, 0.0, 0.0)
z2 = mlab.bivariate_normal(0, 2 * sigma, sigma, sigma, 0.0, 0.0)
z3 = mlab.bivariate_normal(0, 3 * sigma, sigma, sigma, 0.0, 0.0)

plt.figure()
#plot Gaussian:
im = plt.imshow(Z, interpolation='bilinear', origin='lower',
                 extent=(-50,50,-50,50),cmap=cm.gray)
#Plot contours at whatever z values we want:
plt.contour(Z, [z3, z2, z1], origin='lower', extent=(-50,50,-50,50),colors='red')
#plt.savefig('fig.png')
plt.show()