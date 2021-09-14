# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 21:03:16 2021

@author: Mahfuz_Shazol
"""

import numpy as np
import tensorflow as tf

I=np.array([[1,0,0],
            [0,1,0],
            [0,0,1]
            ])
I_tf=tf.convert_to_tensor(I)

A=np.array([[1,2,3]]).T
A_tf=tf.convert_to_tensor(A)

result=tf.matmul(I_tf, A_tf)
print(result)
