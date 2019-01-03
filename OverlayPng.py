# coding: utf-8

from PIL import Image
import os

image_folder = '/////////////'
players_name = []

# フォルダ名取得
for i in os.listdir(image_folder):
    if not os.path.isfile(image_folder + i):
        players_name.append(i)


players_images = [[] for j in range(5)]

for f in range(len(players_name)):
    players_img_dir = image_folder + "/" + players_name[f] + "/"
    for i in os.listdir(players_img_dir):
        if os.path.splitext(players_img_dir + i)[-1] == '.png':
            players_images[f].append(players_img_dir + i)



os.mkdir("overlayed")
for i in range(len(players_images[1])):
    result = Image.new('RGBA', (1920,1080), (255,255,255,0))
    for j in range(len(players_name)):
        layer = Image.open(players_images[j][i])
        overlay = Image.new('RGBA', layer.size, (255,255,255,0))
        overlay.paste(layer, (0,0), layer)
        result = Image.alpha_composite(result, overlay)
    result.save('overlayed/result-{0:03d}.png'.format(i))
