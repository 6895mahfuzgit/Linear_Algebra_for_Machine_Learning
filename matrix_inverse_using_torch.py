# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 00:06:29 2021

@author: Mahfuz_Shazol
"""

import numpy as np
import torch as th

X=np.array([[4.,2],[-5,-3]])
X_th=th.as_tensor(X)
X_th_inv=th.inverse(X_th)
print('Inverse of X ',X_th_inv)
Y=np.array([4.,-7])
Y_th=th.as_tensor(Y)

 #w=(X**-1)Y
result=th.matmul(X_th_inv,Y_th)
print(result)


#Y=Xw
result_y=th.matmul(X_th,result)
print(result_y)