# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:42:17 2021

@author: Mahfuz_Shazol
"""

import numpy as np

#transposition a regular 1-D array has no effect
x_array=np.array([1,2,4])
x_t=x_array.T
print(x_t)


y_array=np.array([[1,2,4]])
y_t=y_array.T
print(y_t.shape)
print(y_t)

#back to it's original form
print(y_t.T)
print(y_t.T .shape)

#create  zero vector in numpy
zero_t=np.zeros(5)
print(zero_t)


