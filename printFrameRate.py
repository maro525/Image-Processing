import cv2
import imutils
from imutils.video import VideoStream
import time

# cap = cv2.VideoCapture(0)
cap = VideoStream(src=0).start()
time.sleep(2.0)

tm = cv2.TickMeter()
tm.start()

count = 0
max_count = 10
fps = 0

while True:
    # ret, frame = cap.read()
    frame = cap.read()

    if count == max_count:
        tm.stop()
        fps = max_count / tm.getTimeSec()
        tm.reset()
        tm.start()
        count = 0

    cv2.putText(frame, 'FPS: {:.2f}'.format(fps),
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv2.imshow('frame', frame)
    print('framerate', fps)
    count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.detroyWindow('frame')

print(cap.get(cv2.CAP_PROS_FPS))
