# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 01:25:36 2021

@author: Mahfuz_Shazol
"""

# frommula A^+ =VD^+ U^T

import numpy as np

A=np.array([
            [-1,2],
            [3,-2],
            [5,7]
           ])

U ,d ,VT =np.linalg.svd(A)
  
D=np.diag(d)
print(D)

D_inv=np.linalg.inv(D)
print(D_inv)

print(A.shape[0])
print(A.shape[1])

D_plus=np.zeros((3,2)).T
print(D_plus)

D_plus[:2,:2]=D_inv
print(D_plus)

result=np.dot(VT.T,np.dot(D_plus,U.T))

print('A^+',result)

#numpy has build in function
result=np.linalg.pinv(A)
print(result)




