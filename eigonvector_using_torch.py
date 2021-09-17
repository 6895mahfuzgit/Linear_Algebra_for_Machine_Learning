# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 02:53:27 2021

@author: Mahfuz_Shazol
"""

import numpy as np
import torch as th
A=np.array([
    [-1.,4],
    [2,-2]
    ])

A_th=th.as_tensor(A);

eigons=th.eig(A_th,eigenvectors=True)
print('lambdas',eigons)

v_th=eigons.eigenvectors[:,0]
lmbda=eigons.eigenvalues[0][0]
print('lmbda',lmbda)

#A**v==Lamda**v
r1=th.matmul(A_th,v_th)
print('A**v=',r1)

r2=lmbda*v_th
print(r2)


