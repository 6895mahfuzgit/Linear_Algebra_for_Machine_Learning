# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 23:40:54 2021

@author: Mahfuz_Shazol
"""

import tensorflow as tf

X=tf.Variable([[1.,2],[3,4]])

result=tf.norm(X)

print('******** Result ********:-',result)

