# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 01:16:05 2021

@author: Mahfuz_Shazol
"""

import numpy as np

#formula  A=V (A_lambda(Diagonal Matrix)) V**-1


A=np.array([
            [4.,2],
            [-5,-3]
          ])

#V
lambdas,V=np.linalg.eig(A) 
#V**-1
inv_V=np.linalg.inv(V)


diago_lambdas=np.diag(lambdas)

result=np.dot(V,np.dot(diago_lambdas,inv_V))
print(result)

print(result==A)

