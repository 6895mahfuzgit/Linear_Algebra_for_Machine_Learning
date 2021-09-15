# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 23:38:53 2021

@author: Mahfuz_Shazol
"""

import numpy as np 
import torch as th

X=np.array([[1.,2],[3,4]])
X_th=th.as_tensor(X)
result=th.norm(X_th)

print(result)
