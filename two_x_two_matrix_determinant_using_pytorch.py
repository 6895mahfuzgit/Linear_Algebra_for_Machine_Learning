# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 01:06:38 2021

@author: Mahfuz_Shazol
"""

import numpy as np
import torch as th

X=np.array([
    [4.,2],
    [-5,-3]
    ])

result =th.det(th.as_tensor(X))
print(result)



N=np.array([
    [-4.,1],
    [-8,2]
    ])

result =th.det(th.as_tensor(N))
print(result)