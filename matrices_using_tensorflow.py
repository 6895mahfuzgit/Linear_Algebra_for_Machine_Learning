# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 01:49:30 2021

@author: Mahfuz_Shazol
"""

import tensorflow as tf


x_tf=tf.Variable([ [1,0],
            [5,4],
            [8,9],
            [1,2],
            ]);



print(tf.shape(x_tf))

print('size',tf.rank(x_tf))

#get all first row items
print(x_tf[:,0])

#get 3rd row items
print(x_tf[2,:])

#slicing by index_tf
print(x_tf[1:3])