# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 01:29:59 2021

@author: Mahfuz_Shazol
"""

import numpy as np


X=np.array([ [1,0],
            [5,4],
            [8,9],
            [1,2],
            ]);


print(X.shape)
print('size',X.size)

#get all first row items
print(X[:,0])

#get 3rd row items
print(X[2,:])

#slicing by index
print(X[1:3])



