# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 02:37:53 2021

@author: Mahfuz_Shazol
"""

import numpy as np

A=np.array([
    [-1,4],
    [2,-2]
    ])

lambdas,V=np.linalg.eig(A)
print('lambdas',lambdas)

#each column is separate eivactor V
print('V',V)

#A**v==Lamda**v

v=V[:,0]
print(v)
Lamda=lambdas[0]

r1=np.dot(A,v)
print(r1)

r2=np.dot(Lamda,v)
print(r2)
