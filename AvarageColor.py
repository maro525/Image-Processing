# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('lena.jpg')

average_color_per_row = np.average(img, axis=0)
average_color = np.average(average_color_per_row, axis=0)
average_color = np.uint8(average_color)
average_color_img = np.array([[average_color]*500]*500, np.uint8)

cv2.imshow('average', average_color_img)
# cv2.imwrite('average.png', average_color_img)
cv2.waitKey(0)