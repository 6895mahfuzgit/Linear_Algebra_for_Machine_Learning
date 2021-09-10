# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 02:44:18 2021

@autfor: Mahfuz_Shazol
"""

import tensorflow as tf


X_tf=tf.Variable([[12,56],
            [6,44],
            [1,96],
            ])

A_tf=X_tf+2*3

#A_tfdd
A_tfdd_result=X_tf+A_tf
print('A_tffter A_tfdd ',A_tfdd_result)
print()
print()

#Multi
multi_result=X_tf+A_tf
print('A_tffter multi ',multi_result)
print()
print()

#Div
div_result=X_tf/A_tf
print('A_tffter div ',div_result)
print()
print()

#sub
sub_result=A_tf-X_tf
print('A_tffter sub ',sub_result)
print()
print()
