# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:58:07 2021

@author: Mahfuz_Shazol
"""

import numpy as np
import torch as th

I=np.array([[1,0,0],
            [0,1,0],
            [0,0,1]
            ])
I_th=th.as_tensor(I)

A=np.array([[1,2,3]]).T
A_th=th.as_tensor(A)

result=th.matmul(I_th,A_th)
print(result)
