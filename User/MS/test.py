import cv2
import os
import sys
import numpy as np

face_classifier = cv2.CascadeClassifier('/home/gigachany/anaconda3/envs/gigachany/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

def face_detector(img, size = 0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3, 5)
    if faces is () :
        return None 
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)
        face = img[y:y + h, x:x + w]
        face = cv2.resize(face,(200, 200))
    return img, face   

def Gender_Checker(image, number):
    img, face = face_detector(image)
    ModelName = ["human_female.yml", "human_male.yml"]
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        model = cv2.face.LBPHFaceRecognizer_create()
        model.read("/home/gigachany/CODE/model/"+ModelName[number])
        result = model.predict(face)
        if result[1] < 500 :
            confidence = int(100 * (1 - (result[1]) / 300))
            display_string = str(confidence) + '%'
        print("Check Complete")
        return confidence
    except:
        print("Face Not Found")
        pass 

def Checker_Output(A, B):
    if A > B : print("삐빅! 사진의 인물은 여성입니다.")
    elif A < B : print("삐빅! 사진의 인물은 남성입니다.")
    else : print("삐빅! 반반입니다.")

if __name__ == "__main__":
    path = '/home/gigachany/CODE/GiGAChany/SendImage/images.jpg'
    image = cv2.imread(path)
    print("Wait..")
    Checker_Output(Gender_Checker(image, 0), Gender_Checker(image, 1))

