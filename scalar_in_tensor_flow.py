# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 01:59:07 2021

@author: Mahfuz_Shazol
"""

import tensorflow as tf

print(tf.version.VERSION)

x_tf=tf.Variable(25 ,dtype=tf.int16)
print(x_tf)
print(x_tf.shape)

y_tf=tf.Variable(10,dtype=tf.int16)
print(x_tf+y_tf)

result_tf=tf.add(x_tf, y_tf)
print('result_tf  :- ',result_tf)

#Convert Tensor to Numpy

result_tf.numpy()
print('Numpy Result:- ',result_tf.numpy())

print('Type After Convertion:- ',type(result_tf.numpy()))


tf_float=tf.Variable(53,dtype=tf.float16)

print(tf_float)
