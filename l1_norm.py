# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 00:33:23 2021

@author: Mahfuz_Shazol
"""

import numpy as np 

array=[25,2,5]

result=0
for i in array:
    result+=np.abs(i)
print(result)