#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 23:27:06 2024

@author: reggiehacker
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

rng = np.random.default_rng()

#Define two seperates lists, one for each direction
y = rng.random(500) > 0.5
x = rng.random(500) > 0.5
z = rng.random(500) > 0.5

#Make them negative 1 or positive 1
y = 2*y - 1
x = 2*x - 1
z = 2*z - 1

#add lists together to find final coords
x = np.cumsum(x)
y = np.cumsum(y)
z = np.cumsum(z)

#plot coords using Axes3D
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
ax1.plot(x, y, z)  

plt.show()