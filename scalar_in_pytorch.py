# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 01:44:45 2021

@author: Mahfuz_Shazol
"""

import torch

#x_pt=torch.tensor(25)
x_pt=torch.tensor(25,dtype=torch.float16)
print(x_pt)
print(type(x_pt))

print(x_pt.shape)