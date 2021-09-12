# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 02:02:48 2021

@author: Mahfuz_Shazol
"""

import tensorflow as tf

x=tf.Variable([
          [3,4],
          [5,6],
          [7,8]
         ])

y=tf.Variable([1,2])

result=tf.linalg.matvec(x, y)
print(result)