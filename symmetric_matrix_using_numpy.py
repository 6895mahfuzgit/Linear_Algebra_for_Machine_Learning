# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:02:09 2021

@author: Mahfuz_Shazol
"""

import numpy as np

A=np.array([[1,4,6],
            [4,2,7],
            [6,7,3]
            ])

A_T=A.T
print(A_T)
print(A==A_T)