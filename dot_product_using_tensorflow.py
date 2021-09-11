# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 02:15:53 2021

@author: Mahfuz_Shazol
"""

import tensorflow as tf

x=tf.Variable([1,2,3])
y=tf.Variable([7,8,9])
result=tf.reduce_sum(tf.multiply(x, y))
print(result)