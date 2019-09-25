import cv2
import os
import sys
import numpy as np

face_classifier = cv2.CascadeClassifier('/home/gigachany/anaconda3/envs/gigachany/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

def face_detector(img, size = 0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3, 5)
    if faces is ():
        return None 
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)
        face = img[y:y + h, x:x + w]
        face = cv2.resize(face,(200, 200))
    return img, face    

if __name__ == "__main__":
    path = '/home/gigachany/CODE/GiGAChany/Test_JPG/images.jpg'
    image = cv2.imread(path)
    img, face = face_detector(image)
    
    #try:
    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    model = cv2.face.LBPHFaceRecognizer_create()
    model = model.read('/home/gigachany/CODE/GiGAChany/model/human_female.yml')
    result = model.predict(face)
    print(result[1])
    if result[1] < 500:
        confidence = int(100 * (1 - (result[1]) / 300))
        display_string = str(confidence) + '%'
        print(display_string)
    if confidence > 50:
        print("FEMALE")
    else:
        print("NOT FEMALE")
    # except:
    #     print("Face Not Found")
    #     pass