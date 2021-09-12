# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 01:58:53 2021

@author: Mahfuz_Shazol
"""

import torch as th

x=th.tensor([
          [3,4],
          [5,6],
          [7,8]
         ])

y=th.tensor([1,2])

result=th.matmul(x,y)
print(result)
