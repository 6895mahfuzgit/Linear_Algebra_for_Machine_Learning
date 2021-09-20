# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 00:58:09 2021

@author: Mahfuz_Shazol
"""

import numpy as np

X=np.array([
            [1,2,4],
            [2,-1,3],
            [0,5,1]
          ])


det_x_result=np.linalg.det(X)
print(det_x_result)


lambdas,v=np.linalg.eig(X)
product_of_eigon_result=np.product(lambdas)
print(product_of_eigon_result)

