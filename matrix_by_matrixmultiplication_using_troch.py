# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 01:15:21 2021

@author: Mahfuz_Shazol
"""

import numpy as np
import torch as th

A=np.array([
           [3,4],
           [5,6],
           [7,8],
          ])

B=np.array([
            [1,9],
            [2,0],
          ])


A_th=th.from_numpy(A)
print(A_th)
B_th=th.as_tensor(B,dtype=th.int32)
print(B_th)
result=th.matmul(A_th,B_th)
print(result)



