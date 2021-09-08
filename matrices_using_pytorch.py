# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 01:46:42 2021

@author: Mahfuz_Shazol
"""

import torch as th


x_th=th.tensor([ [1,0],
            [5,4],
            [8,9],
            [1,2],
            ]);


print(x_th.shape)

#get all first row items
print(x_th[:,0])

#get 3rd row items
print(x_th[2,:])

#slicing by index_th
print(x_th[1:3])