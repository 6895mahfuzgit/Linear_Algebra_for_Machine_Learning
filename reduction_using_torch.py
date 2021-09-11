# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 19:25:58 2021

@author: Mahfuz_Shazol
"""

import torch as th
 
X = th.tensor([[50.1, 15, 89, 23, 64], 
              [45, 98, 25, 17, 55], 
              [35, 37, 9, 100, 61]])


sum_result=X.sum()
print(sum_result)


#sum all rows
row_sum_result=X.sum(axis=0)
print(row_sum_result)


#sum all cols
col_sum_result=X.sum(axis=1)
print(col_sum_result)

#max
max_result=X.max();
print(max_result)
#max in rows
max_row_result=th.max(X,axis=0)
print('max_row_result',max_row_result)
#max in cols
max_col_result=th.max(X,axis=1)
print('max_row_result',max_col_result)

#min 
min_result=X.min();
print(min_result)
#min  in rows
min_row_result=th.min(X,axis=0);
print('min_row_result',min_row_result)
min_col_result=th.min(X,axis=1);
print('min_row_result',min_col_result)

#mean
mean_result=th.mean(X);
print('mean_result',mean_result)
#mean in rows
mean_row_result=th.mean(X,axis=0)
print('mean_row_result',mean_row_result)
#mean in cols
mean_col_result=th.mean(X,axis=1)
print('mean_col_result',mean_col_result)


#product
product_result=X.prod();
print('product_result',product_result)
#mean in rows
product_row_result=th.prod(X,axis=0)
print('product_row_result',product_row_result)
#mean in cols
product_col_result=th.prod(X,axis=1)
print('product_col_result',product_col_result)





