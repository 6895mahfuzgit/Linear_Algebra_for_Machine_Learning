# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 01:12:41 2021

@author: Mahfuz_Shazol
"""

import numpy as np

A=np.array([
           [3,4],
           [5,6],
           [7,8],
          ])

B=np.array([
            [1,9],
            [2,0],
          ])


result=np.dot(A,B)

print(result)
