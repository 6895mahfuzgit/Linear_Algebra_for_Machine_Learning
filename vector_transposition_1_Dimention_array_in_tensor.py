# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 23:01:02 2021

@author: Mahfuz_Shazol
"""

import tensorflow as tf


x_tf=tf.Variable([1,2,3,4],dtype=tf.int16)
print(tf.transpose(x_tf))
print(tf.transpose(x_tf).shape)


y_tf=tf.Variable([[1,2,3,4]])
print(tf.transpose(y_tf))
print(tf.transpose(y_tf).shape)


z_tf=tf.transpose(y_tf)
print(tf.transpose(z_tf))
print(tf.transpose(z_tf).shape)