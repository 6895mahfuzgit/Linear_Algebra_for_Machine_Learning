# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 03:11:59 2021

@author: Mahfuz_Shazol
"""
import tensorflow as tf
A=tf.Variable([
    [-1.,4],
    [2,-2]
    ])

lmbd,V=tf.linalg.eig(A)
print(lmbd)
v=V[:,0]

lm1=lmbd[0]
print(lm1)


#A**v==Lamda**v
r1=lm1*v
r2= A * tf.cast(v,dtype=tf.float32)



