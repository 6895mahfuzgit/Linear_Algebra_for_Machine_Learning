# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 02:09:53 2021

@author: Mahfuz_Shazol
"""

import numpy as np
import torch as th

A=np.array([[25,2],
            [5,4]])

A_trace=np.trace(A)
print(A_trace)

# Tr(A)=Tr(A.T)
result1=np.trace(A)
print(result1)
result2=np.trace(A.T)
print(result2)
print('Tr(A)=Tr(A.T)   Ans:',result1==result2)


#Calculate Frobenius norm AF=(Tr(A A.T))**(1/2)
A_p=th.tensor([
    [-1,2],
    [3,-2],
    [5,7],
    ])


calculated_frobenius_norm=(th.trace(th.matmul(th.as_tensor(A),th.as_tensor(A.T))))**(1/2)
print('calculated_frobenius_norm  Ans:',calculated_frobenius_norm)

norm_result=np.linalg.norm(A)
print(norm_result)









    


