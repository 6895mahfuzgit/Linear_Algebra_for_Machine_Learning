# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 19:42:02 2021

@autfor: Mahfuz_Shazol
"""

import  tensorflow as tf

X = tf.Variable([[50.1, 15, 89, 23, 64], 
              [45, 98, 25, 17, 55], 
              [35, 37, 9, 100, 61]])


sum_result=tf.reduce_sum(X)
print(sum_result)


#sum all rows
row_sum_result=tf.reduce_sum(X,axis=0)
print(row_sum_result)


#sum all cols
col_sum_result=tf.reduce_sum(X,axis=1)
print(col_sum_result)

#max
max_result=tf.reduce_max(X);
print(max_result)
#max in rows
max_row_result=tf.reduce_max(X,axis=(0));
print('max_row_result',max_row_result)
#max in cols
max_col_result=tf.reduce_max(X,axis=(1));
print('max_row_result',max_col_result)

#min 
min_result=tf.reduce_min(X);
print(min_result)
#min  in rows
min_row_result=tf.reduce_min(X,axis=0);
print('min_row_result',min_row_result)
min_col_result=tf.reduce_min(X,axis=1);
print('min_row_result',min_col_result)

#intensor it refuse to calculate int type so give float type
#mean
mean_result=tf.reduce_mean(X);
print('mean_result',mean_result)
#mean in rows
mean_row_result=tf.reduce_mean(X,axis=0)
print('mean_row_result',mean_row_result)
#mean in cols
mean_col_result=tf.reduce_mean(X,axis=1)
print('mean_col_result',mean_col_result)


#product
product_result=tf.reduce_prod(X);
print('product_result',product_result)
#mean in rows
product_row_result=tf.reduce_prod(X,axis=0)
print('product_row_result',product_row_result)
#mean in cols
product_col_result=tf.reduce_prod(X,axis=1)
print('product_col_result',product_col_result)