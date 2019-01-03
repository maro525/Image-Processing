# coding: utf-8

import cv2
import numpy as np

if __name__ == '__main__':

    # 画像読み込み
    img_vacant = cv2.imread("img/vacant.png")
    img_used = cv2.imread("img/not_vacant.png")

    img_diff = cv2.absdiff(img_used, img_vacant)
    # cv2.imshow("img_diff", img_diff)
    # print(img_diff)
    print(img_diff.shape)

    print(np.count_nonzero(img_diff))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
