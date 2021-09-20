# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 01:16:05 2021

@author: Mahfuz_Shazol
"""

import numpy as np

#formula  A=V (A_lambda(Diagonal Matrix)) V**-1


A=np.array([
            [4.,2.],
            [-5.,-3.]
          ])

print(A)
#V
lambdas,V=np.linalg.eig(A) 
#V**-1
inv_V=np.linalg.inv(V)


diago_lambdas=np.diag(lambdas)

result=np.dot(V,np.dot(diago_lambdas,inv_V))
print(result)

print((A==result).all())




#if A is real No matrix then without using inverse we can Tanspose like
# formula  A= Q (A_lambda(Diagonal Matrix)) Q**T

A=np.array([
            [2.,1],
            [1.,2]
          ])


lambdas,Q=np.linalg.eig(A)
A_lambda=np.diag(lambdas)
Q_T=Q.T

result_of_real_matrix=np.dot(Q,np.dot(A_lambda,Q_T))
print(result_of_real_matrix)
print((A==result_of_real_matrix).all())









