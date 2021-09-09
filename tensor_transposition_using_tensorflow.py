# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 02:23:05 2021

@author: Mahfuz_Shazol
"""
import tensorflow  as tf


x=tf.Variable([
                [8,4],
                [1,5],
                [9,3],
                 ])


result=tf.traspose(x)

print(result)