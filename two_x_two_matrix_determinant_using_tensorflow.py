# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 01:10:08 2021

@author: Mahfuz_Shazol
"""

import numpy as np
import tensorflow as tf

X=tf.Variable([
    [4.,2],
    [-5,-3]
    ])

result =tf.linalg.det(X)
print(result)



N=tf.Variable([
    [-4.,1],
    [-8,2]
    ])

result =tf.linalg.det(N)
print(result)