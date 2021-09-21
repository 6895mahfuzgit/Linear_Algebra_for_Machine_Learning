# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 23:24:13 2021

@author: Mahfuz_Shazol
"""

import time
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import imageio

img=Image.open('1631457997498.jpg')
# plt.imshow(img)

imggray=img.convert('LA')
plt.imshow(imggray)

imgmat=np.array(list(imggray.getdata(band=0)),float)
#print(imgmat)
#print(imggray.size[1],imggray.size[0])
imgmat.shape=imggray.size[1],imggray.size[0]

imgmat=np.matrix(imgmat)
plt.imshow(imgmat,cmap='gray')
#print(imgmat)

U, sigma, V=np.linalg.svd(imgmat)

# resonstract_img=np.matrix(U[:,:1]) * np.diag(sigma[:1]) * np.matrix(V[:1,:])
# plt.imshow(resonstract_img,cmap='gray')

# for i in [2,4,8,16,32,64]:
#     resonstract_img=np.matrix(U[:,:i]) * np.diag(sigma[:i]) * np.matrix(V[:i,:])
#     plt.imshow(resonstract_img,cmap='gray') 

resonstract_img=np.matrix(U[:,:128]) * np.diag(sigma[:128]) * np.matrix(V[:128,:])    


cImg=Image.fromarray(resonstract_img)
#cImg=cImg.convert('L')
#plt.imshow(cImg)
imageio.imwrite('compressedImage.jpeg', cImg)

