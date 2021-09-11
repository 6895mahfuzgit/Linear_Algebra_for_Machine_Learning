# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 02:13:55 2021

@author: Mahfuz_Shazol
"""

import torch as th


x=th.tensor([1,2,3])
y=th.tensor([7,8,9])

result=th.dot(x,y)
print(result)