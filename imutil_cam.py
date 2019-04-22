from imutils.video import VideoStream
import imutils
import cv2
import time

vs = VideoStream(src=0).start()
tm = cv2.TickMeter()
tm.start()

count = 0
max_count = 10
fps = 0
bCalc = False

while True:
    frame = vs.read()
    if bCalc is False:
        originW = frame.shape[1]
        print('Original Camera Width', originW)
        bCalc = True
    frame = imutils.resize(frame, width=400)

    if count == max_count:
        tm.stop()
        fps = max_count / tm.getTimeSec()
        tm.reset()
        tm.start()
        count = 0

    cv2.imshow("frame", frame)
    key = cv2.waitKey(1) & 0xFF

    print('framerate', fps)
    count += 1

cv2.destroyAllWindows()
vs.stop()
