# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 22:56:20 2021

@author: Mahfuz_Shazol
"""

import numpy as np


#formula   A=U D V^T

A=np.array([
            [-1,2.],
            [3,-2],
            [5,7]
         ])

U , d,VT=np.linalg.svd(A)

print('U :-',U)
print('VT :-',VT)
print('d :-',d)

print('np.diag(d) :-',np.diag(d))
D=np.concatenate((np.diag(d),[[0,0]]),axis=0)
print('D',D)

result=np.dot(U,np.dot(D,VT))
print(result)