#coding: utf-8

# http://derivecv.tumblr.com/post/73561473978

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)
tm = cv2.TickMeter()
tm.start()

count = 0
max_count = 10
fps = 0

while(True):
    ret, frame = cap.read()

    if count == max_count:
        tm.stop()
        fps = max_count / tm.getTimeSec()
        tm.reset()
        tm.start()
        count = 0

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    print('framerate', fps)
    count += 1

# すべての処理が終了した後はストリームを開放
cap.release()
cv2.destroyAllWindows()
