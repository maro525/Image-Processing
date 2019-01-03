#!/usr/bin/env python
#-*- encoding: utf-8 -*-

#opencvの動作を確認するためのプログラム
#画像の表示
#http://lp-tech.net/archives/1975

# import cv
import cv2

img = cv2.imread("image/lena.jpg")
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
