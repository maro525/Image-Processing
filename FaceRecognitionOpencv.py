#-*- encoding:utf-8 -*-

#顔認識プログラム
#http://lp-tech.net/archives/2186

import numpy as np
#import cv
import cv2
from PIL import Image

def get_face(picture_name):
	cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
	image = cv2.imread(str(picture_name))
	cascade = cv2.CascadeClassifier(cascade_path)
	color = (255,0,0)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#cv2.cv.CV_BGR2GRAYは、cv2.COLOR_BGR2GRAYに変わった
	facerect = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(1,1))
	if len(facerect) > 0:
		for rect in facerect:
			cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
	else:
		print("no face")
	cv2.imshow("detect.jpg", image)
	cv2.waitKey(0)

if __name__ == '__main__':
	get_face("image/face_01.jpg")

