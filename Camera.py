#coding: utf-8

#http://derivecv.tumblr.com/post/73561473978

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#すべての処理が終了した後はストリームを開放
cap.release()
cv2.destroyAllWindows()
