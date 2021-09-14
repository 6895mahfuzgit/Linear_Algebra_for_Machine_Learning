# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:18:42 2021

@author: Mahfuz_Shazol
"""

import numpy as np
import torch as th
A=np.array([[1,4,6],
            [4,2,7],
            [6,7,3]
            ])

A_th=th.as_tensor(A,dtype=th.int32)
A_th_T=A_th.T
print(A_th==A_th_T)