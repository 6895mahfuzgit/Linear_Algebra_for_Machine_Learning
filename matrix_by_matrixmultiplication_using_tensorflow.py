# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 01:26:24 2021

@author: Mahfuz_Shazol
"""

import numpy as np
import tensorflow as tf

A=np.array([
           [3,4],
           [5,6],
           [7,8],
          ])

B=np.array([
            [1,9],
            [2,0],
          ])


A_tf=tf.convert_to_tensor(A)
B_tf=tf.convert_to_tensor(B)

result=tf.matmul(A_tf,B_tf)
print(result)


