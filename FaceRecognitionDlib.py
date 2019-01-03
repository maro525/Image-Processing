# coding: utf-8

import cv2
import dlib

sample_img_path = 'img/obama.jpg'

def facedetector_dlib(img, img_path):
    try:
        detector = dlib.get_frontal_face_detector()
        # rgb変換 (opencv形式からskimage形式に変換)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # frontal_face_detecotrクラスは矩形、スコア、サブ検出器の結果を返す
        dets, scores, idx = detector.run(img_rgb, 0)
        # 矩形の色
        color = (0, 0, 255)
        s = ''
        if len(dets) > 0:
            # 顔画像ありのとき
            for i, rect in enumerate(dets):
                # detsが矩形、scoreはスコア、idxはサブ検出器の結果
                cv2.rectangle(img, (rect.left(), rect.top()), (rect.right(), rect.bottom()), color, thickness=10)
                s += (str(rect.left()) + ' ' + str(rect.top()) + '' + str(rect.right()) + ' ' + str(rect.bottom()) + ' ')
            s += image_path
        # 矩形が書き込まれた画像とs = 'x1 y1 x2 y2 x1 y1 x2 y2 file_name'
        # 顔がなければ s = '' が帰る
        return img, s

    except:
        return img, ""

if __name__ == '__main__':
    img = cv2.imread(sample_img_path)
    img, s = facedetector_dlib(img, sample_img_path)
    cv2.imwrite('output_' + sample_img_path, img)
    f = open('./rect.txt', 'w')
    f.write(s)
    f.close()
