#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import sys

if __name__ == '__main__':

    video = cv2.VideoCapture('../video/basket.mp4')


    if not video.isOpened():
        print("could not open video")
        sys.exit()

    ok, frame = video.read()
    if not ok:
        print("cannot read video file")
        sys.exit()

    cv2.imshow("select face", frame)
    roi = cv2.selectROI('Target', frame)
    tracker = cv2.TrackerMedianFlow_create()
    ok = tracker.init(frame, roi)

    while True:
        ok, frame = video.read()
        if not ok:
            break

        # start timer
        timer = cv2.getTickCount()

        # update tracker
        ok, roi = tracker.update(frame)

        # calculate the frames per second
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

        # draw bounding box
        if ok:
            p1 = (int(roi[0]), int(roi[1]))
            p2 = (int(roi[0] + roi[2]), int(roi[1] + roi[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0,), 2, 1)
        else:
            cv2.putText(frame, "Tracking failure", (100, 80), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0,0,255), 2)

        # display tracker type on frame
        cv2.putText(frame, 'GOTURN' + 'Tracker', (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)

        # disokay fps on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

        # Display result
        cv2.imshow("Target", frame)

        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27: break
