# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 02:13:31 2021

@author: Mahfuz_Shazol
"""

import tensorflow as tf

X=tf.Variable([[12,56],
            [6,44],
            [1,96],
            ])

#add
X_additionX=X+2
print('After add ',X_additionX)
print()
print()
#another way of add
X_addition2=tf.add(X,2)
print('After add(anothet) ',X_addition2)
print()
print()



#Multi
X_multi=X*2
print('after multi ',X_multi)
print()
print()
#another way of Multi
X_multi_2=tf.multiply(X,2)
print('after multi(another) ',X_multi_2)
print()
print()


#Div
X_div=X/2
print('after div ',X_div)
print()
print()
#another way of div
X_div_2=tf.divide(X,2)
print('after div(another) ',X_div_2)
print()
print()


#sub
X_sub=X-1
print('after sub ',X_sub)
print()
print()
#another way of sub
X_div_2=tf.subtract(X,1)
print('after sub(another) ',X_div_2)
print()
print()


#multi Operations 
X_result= X*2+1
print('result ',X_result)
print()
print()
#multi Operations in another way
X_result_2=tf.add(tf.multiply(X,2),1)
print('result(another) ',X_result_2)
print()
print()

