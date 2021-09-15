# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 00:13:52 2021

@author: Mahfuz_Shazol
"""
import tensorflow as tf

X=tf.Variable([[4.,2],[-5,-3]])
X_inv=tf.linalg.inv(X)

Y=tf.Variable([4.,-7])

#w=(X**-1)Y
result=tf.matmul(X_inv,Y)
print(result)
 

#Y=Xw

