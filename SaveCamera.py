# coding: UTF-8
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
out = cv2.VideoWriter('output.avi',0,20,(640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2 .destroyAllWindows()