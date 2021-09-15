# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 23:33:32 2021

@author: Mahfuz_Shazol
"""

import numpy as np 

X=np.array([[1,2],[3,4]])

#frobenius_norm_frommula=(1**2+2**2+3**2+4**2)**(1/2)
#print(frobenius_norm_frommula)

#using numpy
result=np.linalg.norm(X)
print(result)
