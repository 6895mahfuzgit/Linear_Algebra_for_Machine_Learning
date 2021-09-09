# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 02:21:33 2021

@author: Mahfuz_Shazol
"""

import torch as th

x=th.tensor([
              [1,2],
              [3,7],
              [9,4],
            ])

result=x.T
print(result)