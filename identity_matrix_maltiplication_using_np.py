# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:55:18 2021

@author: Mahfuz_Shazol
"""

import numpy as np

I=np.array([[1,0,0],
            [0,1,0],
            [0,0,1]
            ])

A=np.array([[1,2,3]]).T
            
result=np.dot(I,A)        
print(result)
