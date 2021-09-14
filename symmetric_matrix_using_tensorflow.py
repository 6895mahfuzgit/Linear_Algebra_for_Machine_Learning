# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:26:56 2021

@author: Mahfuz_Shazol
"""


import numpy as np
import tensorflow as tf

A=np.array([[1,4,6],
            [4,2,7],
            [6,7,3]
            ])


A_tf=tf.convert_to_tensor(A)

A_tf_T=tf.transpose(A_tf)

print(A_tf==A_tf_T)