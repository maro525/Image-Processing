# coding: utf-8

import cv2
import numpy as np

if __name__ == '__main__':

    img_vacant = cv2.imread("book1.jpg")
    img_used = cv2.imread("book1.jpg")

    img_diff = cv2.absdiff(img_vacant, img_used)
    cv2.imshow("img_diff", img_diff)

    img_diffm = cv2.threshold(img_diff, 20, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow("img_diffm", img_diffm)

    # 膨張処理、収縮処理を施してマスク画像を作成
    operator = np.ones((3, 3), np.uint8)
    img_dilate = cv2.dilate(img_diffm, operator, iterations=4)
    img_mask = cv2.erode(img_dilate, operator, iterations=4)
    cv2.imshow("img_dilate", img_dilate)
    cv2.imshow("img_mask", img_mask)

    img_dst = cv2.bitwise_and(img_used, img_mask)

    cv2.imshow("img_dst", img_dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()