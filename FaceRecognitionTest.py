# coding: utf-8

import face_recognition

obama_image = face_recognition.load_image_file("../img/img_people/obama.jpg")
face_locations = face_recognition.face_locations(obama_image)
print(face_locations)

face_encoding = face_recognition.face_encodings(obama_image)
print(len(face_encoding[0]))
