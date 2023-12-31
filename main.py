# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 15:01:24 2023

@author: Amin
"""

from skimage.io import imread, imsave, imshow
import numpy as np
import matplotlib.pyplot as plt


# Gray =  0.299*Red + 0.587*Green + 0.114*Blue
# Gray -> R G B 
pic_colored = imread('1.jpg')
pic_colored = pic_colored.astype('float')
pic_colored /= 255
print(f"Size of original image: {pic_colored.shape}")
pic_gray = np.zeros(pic_colored.shape[:2])
row_gray, col_gray = pic_gray.shape
for r in range(row_gray):
    for c in range(col_gray):
        red = pic_colored[r, c, 0]
        green = pic_colored[r, c, 1]
        blue = pic_colored[r, c, 2]
        gray = 0.299 * red + 0.587 * green + 0.114 * blue
        pic_gray[r, c] = gray
===
imshow(pic_gray)
plt.imsave('1_gray.png', pic_gray, cmap='gray')
