import cv2
import os
import sys
import numpy as np
import socket
import threading
from time import *

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

def Gender_Checker(image, number):
    try:
        if number == 0 : print("Female Check")
        else : print("Male Check")
        img, face = face_detector(image)
        ModelName = ["human_female.yml", "human_male.yml"]
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('/home/gigachany/CODE/GiGAChany/OutImage/images.jpg', face)
        model = cv2.face.LBPHFaceRecognizer_create()
        model.read("/home/gigachany/CODE//model/"+ModelName[number])
        result = model.predict(face)
        if result[1] < 500:
            confidence = int(100 * (1 - (result[1]) / 500))
            display_string = str(confidence) + '%'
        print("Check Complete")
        return confidence
    except:
        print("Face Not Found")
        return 0
        pass 

def Checker_Output(A, B):
    if A == 0 or B == 0 :
        A = 1
        B = 1
    if A > B : 
        return 'female^' + str(A) + '^'
    elif A < B : 
        return 'male^' + str(B) + '^'
    else : 
        return 'fail^' + str(A) + '^'

def Server():
    path = '/home/gigachany/CODE/GiGAChany/SendImage/images.jpg'
    s = socket.socket()
    s.bind(("10.10.20.54", 9078))
    s.listen(10)
    while True: 
        print("test")
        c, address = s.accept()
        print(address)
        f = open(path, 'wb')
        l = c.recv(1024)
        count = 0
        while(l):
            f.write(l)
            count +=1
            if count % 10 == 0 : print("이미지 전송 중 [%d]" %(count))
            l = c.recv(1024)
        print("이미지 전송 완료")
        f.close()
        image = cv2.imread(path)
        test = Checker_Output(Gender_Checker(image, 0), Gender_Checker(image, 1))
        c.close()
        try:
            c, address = s.accept()
            c.send(test.encode())
            c.close()
        except:
            print("Fail")
            pass 
    s.close()

if __name__ == "__main__":
    t = threading.Thread(target = Server)
    t.start()
