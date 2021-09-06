# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:56:11 2021

@author: Mahfuz_Shazol
"""

import torch as th

x_th=th.tensor([1,2,3,4])
print(x_th)
print(type(x_th))
print(x_th.T)
print(x_th.T.shape)

y_th=th.tensor([[1,2,3,4]])
print(y_th)
print(type(y_th))
print(y_th.T)
print(y_th.T.shape)

z_th=y_th.T
print(z_th.T)
print(z_th.T.shape)