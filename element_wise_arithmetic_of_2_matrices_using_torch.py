# -*- coding: utf-8 -*-
"""
CreA_thted on SA_tht Sep 11 02:41:59 2021

@A_thuthor: MA_thhfuz_ShA_thzol
"""

import torch as th


X_th=th.tensor([[12,56],
            [6,44],
            [1,96],
            ])

A_th=X_th+2*3

#A_thdd
A_thdd_result=X_th+A_th
print('A_thfter A_thdd ',A_thdd_result)
print()
print()

#Multi
multi_result=X_th+A_th
print('A_thfter multi ',multi_result)
print()
print()

#Div
div_result=X_th/A_th
print('A_thfter div ',div_result)
print()
print()

#sub
sub_result=A_th-X_th
print('A_thfter sub ',sub_result)
print()
print()
