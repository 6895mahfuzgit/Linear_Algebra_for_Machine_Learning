# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 01:03:24 2021

@author: Mahfuz_Shazol
"""

import numpy as np

X=np.array([
    [4,2],
    [-5,-3]
    ])

result =np.linalg.det(X)
print(result)



N=np.array([
    [-4,1],
    [-8,2]
    ])

result =np.linalg.det(N)
print(result)