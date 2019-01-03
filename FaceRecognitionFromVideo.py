import face_recognition
import cv2
import os
import numpy as np


class Video:
    def __init__(self, num):
        self.camera = cv2.VideoCapture(num) # TODO:カメラのタイプいろいろ対応する。動画データにも対応。

    # ビデオから画像を取る
    def capture(self):
        ret, frame = self.camera.read()
        return frame

    def release(self):
        self.camera.release()


class FaceDetector:
    def __init__(self):
        self.known_faces = {}
        self.tolerance = 0.6

    def load_image_from_folder(self, path):
        for file in face_recognition.image_files_in_folder(path):
            image = face_recognition.load_image_file(file)
            basename = os.path.splitext(os.path.basename(file))[0]
            self.record_face(image, basename)

    def record_face(self, image, name):
        encoding = face_recognition.face_encodings(image)[0]
        self.known_faces.update({name: encoding})

    @staticmethod
    def get_face_encoding(image):
        face_encodings = face_recognition.face_encodings(image)
        return face_encodings

    @staticmethod
    def get_face_location(image):
        face_locations = face_recognition.face_locations(image)
        return face_locations

    # 画像を渡すと、顔の場所と顔の名前が入ったdictを返す
    def analyze_faces_in_image(self, image):
        encodings = self.get_face_encoding(image)
        locations = self.get_face_location(image)
        faces = {}

        if len(self.known_faces) == 0:
            return

        if len(encodings) != 0:
            for encoding, location in zip(encodings, locations):
                compare_encodings = list(self.known_faces.values())
                distance = face_recognition.face_distance(compare_encodings, encoding)
                result = list(distance <= self.tolerance)  # しきい値でふるいにかける
                if True in result:
                    assert isinstance(distance, np.ndarray)
                    name = list(self.known_faces.keys())[distance.argmin()]
                    faces.update({name: location})
        return faces

    def draw_rect(self, image, faces):
        assert isinstance(faces, dict)
        for f in faces:
            cv2.rectangle(image, (faces[f][3], faces[f][0]), (faces[f][1], faces[f][2]), (0, 0, 255), 2)
            cv2.rectangle(image, (faces[f][3], faces[f][2]-25), (faces[f][1], faces[f][2]), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(image, f, (faces[f][3]+6, faces[f][2]-6), font, 0.5, (255, 255, 255), 1)

class Operator:
    def __init__(self):
        video_num = 0
        self.video = None
        self.set_video(video_num)
        self.detector = FaceDetector()

    def set_video(self, num):
        if self.video is None:
            self.video = Video(num)
        else:
            self.video = Video(num)

    def start_video(self):
        self.bVideoRunning = True

    def stop_video(self):
        self.bVideoRunning = False

    # TODO:いろんなデータの読み込み方に対応させる。フォルダ、画像ごと、ウェブからなど。
    def load_data(self):
        img_folder = "../img/img_people"
        self.detector.load_image_from_folder(img_folder)

    def detect_face_in_video(self):
        while self.bVideoRunning:
            image = self.video.capture()
            faces = self.detector.analyze_faces_in_image(image)
            self.detector.draw_rect(image, faces)
            cv2.imshow("frame", image)

            key = cv2.waitKey(1) & 0xff
            if key == ord('q'):
                self.stop_video()
                self.close_window()

    def close_window(self):
        cv2.destroyAllWindows()


if __name__ == '__main__':
    operator = Operator()
    operator.load_data()
    operator.start_video()
    operator.detect_face_in_video()
