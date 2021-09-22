# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 01:41:29 2021

@author: Mahfuz_Shazol
"""

import torch as th

A=th.tensor([
            [-1.,2],
            [3,-2],
            [5,7]
           ])


result=th.pinverse(A)
print(result)