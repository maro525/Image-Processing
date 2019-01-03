#coding: utf-8

# get min&max x, y of image, trim img and export json data

import cv2
import numpy as np
import os
import json

image_folder = 'images'
folders = []

# フォルダ名取得
for i in os.listdir(image_folder):
    if not os.path.isfile(image_folder + "/"+ i):
        folders.append(i)
# print(folders)

# パス取得
players_images = [[] for j in range(5)]
for f in range(len(folders)):
    players_img_dir = image_folder + "/" + folders[f] + "/"
    for i in os.listdir(players_img_dir):
        if os.path.splitext(players_img_dir + i)[-1] == '.png':
            players_images[f].append(players_img_dir + i)
# print(players_images)

# トリミング＆JSONに書き出し
num = 0
player_num = 0

data = {"player": []}
for i in range(5):
	data["player"].append({"data": [], "id": i})

for i in folders:
	num = 0
	for j in players_images[player_num]:
		img = cv2.imread(j, -1)
		size = img.shape
		x_min = 1920
		x_max = 0
		y_min = 1080
		y_max = 0
		y_pixels = []
		for x in range(size[1]):
			for y in range(size[0]):
				rgb_sum = sum(img[y][x])
				if rgb_sum != 0:
					if x < x_min:
						x_min = x
					elif x > x_max:
						x_max = x

					if y < y_min:
						y_min = y
					elif y > y_max:
						y_max = y
		trim = img[y_min:y_max, x_min:x_max]
		print("x_min:{0}, x_max:{1}, y_min:{2}, y_max:{3}".format(x_min, x_max, y_min, y_max))
		dictionary = {"minX": x_min, "maxX": x_max, "minY": y_min, "maxY": y_max}
		data["player"][player_num]["data"].append(dictionary)
		cv2.imwrite('trim/{0}/trim{1:03d}.png'.format(i, num), trim)
		print("player {0} no.{1} image trimmed".format(player_num+1, num))
		num += 1
	player_num += 1

f2 = open('trimmm.json', 'w')
json.dump(data, f2, indent=4, sort_keys=True)
