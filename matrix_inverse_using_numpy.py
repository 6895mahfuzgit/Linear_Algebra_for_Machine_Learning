# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 23:57:35 2021

@author: Mahfuz_Shazol
"""
import numpy as np

X=np.array([[4,2],[-5,-3]])
X_inv=np.linalg.inv(X)
print('Inverse of X ',X_inv)
Y=np.array([4,-7])

#w=(X**-1)Y
result=np.dot(X_inv,Y)
print(result)


#Y=Xw
result_y=np.dot(X,result)
print(result_y)