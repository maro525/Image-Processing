# coding: utf-8

import cv2
import numpy as np

if __name__ == '__main__':

    # カメラ
    cam = cv2.VideoCapture(0)

    # 画像読み込み
    img_vacant = cv2.imread("img/vacant1.png")

    while True:
        img_now = cam.read()[1]
        img_now_resized = cv2.resize(img_now, (800, 504))

        img_diff = cv2.absdiff(img_now_resized, img_vacant)
        cv2.imshow("img_now", img_now_resized)
        #print(img_diff.shape)

        diff_count = np.count_nonzero(img_diff)
        #print(diff_count)

        if diff_count > 500:
            print("not vacant")
        else:
            print("vacant")

        k = cv2.waitKey(1)
        if k == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
