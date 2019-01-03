# coding: utf-8

import cv2
import numpy as np
# from matplotlib import pyplot as plt

# 画像を2値化
def preprocess(img):

    img_grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blured = cv2.GaussianBlur(img_grayed, (5, 5), 0)

    return img_blured

# 2値化
def threshold(preprocessed):
    cv2.imshow("preprocessed", preprocessed)

    # 基本的な2値化
    # under_thresh = 130
    # ret, th = cv2.threshold(preprocessed, under_thresh, 255, cv2.THRESH_BINARY)
    # th = cv2.bitwise_not(th)
    # cv2.imshow("threshold", th)

    # 背景を落としたいとき(明るい部分を落とす)
    # ret, th = cv2.threshold(preprocessed, 200, 255, cv2.THRESH_TOZERO_INV)
    # th = cv2.bitwise_not(th)

    # 大津アルゴリズム
    ret, th = cv2.threshold(preprocessed, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    print(th.size)

    return th

# 青でマスキング
def blue_mask(impath):
    img = cv2.imread(impath)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # threshold for hue channel in blue range
    blue_min = np.array([90, 50, 50], np.uint8)
    blue_max = np.array([130, 255, 255], np.uint8)
    threshold_blue_img = cv2.inRange(img_hsv, blue_min, blue_max)

    cv2.imshow("inrange", threshold_blue_img)

    return threshold_blue_img

# 2値化されたものから輪郭抽出
def contours(threshold, img):
    # find contours
    img, img_contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    print('contours shape : {0}'.format(len(img_contours)))

    # copy the original image
    img_and_contours = np.copy(cv2.imread(img_path))

    # find contours of large enough area
    min_area = 1000
    max_area = 100000
    large_contours = [cnt for cnt in img_contours if cv2.contourArea(cnt) > min_area and cv2.contourArea(cnt) < max_area]

    # draw contours
    cv2.drawContours(img_and_contours, large_contours, -1, (255, 0, 0))
    print('large contours : {0}'.format(len(large_contours)))

    # 外接矩形
    for contour in large_contours:
        # 四角抽出
        # epsilon = 0.05 * cv2.arcLength(contour, True)
        # approx = cv2.approxPolyDP(contour, epsilon, True)
        # print('approx: {0}'.format(approx.shape))
        # if len(approx) == 4:
        #     cv2.drawContours(img_and_contours, [approx], -1, (0, 255, 0), 2)

        # 外接矩形
        # x, y, w, h = cv2.boundingRect(contour)
        # cv2.rectangle(img_and_contours, (x, y), (x + w, y + h), (0, 255, 0), 3)

        # 凸をなくす
        hull = cv2.convexHull(contour)
        cv2.drawContours(img_and_contours, [hull], -1, (0, 255, 0), 2)
        print('hull: {0}'.format(hull.shape))

    return img_and_contours

# エッジ検出
def edge(preprocessed):
    edges = cv2.Canny(preprocessed, 50, 150, apertureSize=3)

    cv2.imshow("edge", edges)
    return edges

# エッジから線分検出
def find_rect(edges, img_path):
    img_and_lines = np.copy(cv2.imread(img_path))

    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    if lines != None:
        for rho, theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))


            cv2.line(img_and_lines, (x1, y1), (x2, y2), (0, 0, 255), 2)


    cv2.imshow("contours", img_and_lines)

    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)
    if lines != None:
        for x1, y1, x2, y2 in lines[0]:
            cv2.line(img_and_lines, (x1, y1), (x2, y2), (0,255,0), 2)

    cv2.imshow("contours", img_and_lines)






img_path = "book1.jpg"
img = cv2.imread(img_path)
cv2.imshow('img', img)

preprocessed = preprocess(img)

threshold = threshold(preprocessed)
contours = contours(threshold, img)

mask = blue_mask(img_path)

edges = edge(preprocessed)

# find_rect(edges, img_path)


# plt.subplot(231), plt.imshow(img, 'original'), plt.title('ORIGINAL')
# plt.subplot(232), plt.imshow(img, 'original'), plt.title('ORIGINAL')
# plt.subplot(233), plt.imshow(img, 'original'), plt.title('ORIGINAL')
# plt.subplot(234), plt.imshow(img, 'original'), plt.title('ORIGINAL')
# plt.subplot(235), plt.imshow(img, 'original'), plt.title('ORIGINAL')
# plt.subplot(236), plt.imshow(img, 'original'), plt.title('ORIGINAL')

# plt.imshow()
