import cv2
import os
import sys
import numpy as np
import socket

face_classifier = cv2.CascadeClassifier('/home/gigachany/anaconda3/envs/gigachany/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
count = 0
def Trainer(name, path, file):
    print("Training Start")
    name += ".yml"
    Data, Labels = [], []
    for i, files in enumerate(file):
        pathI = path + file[i]
        img = cv2.imread(pathI, cv2.IMREAD_GRAYSCALE)
        Data.append(np.asarray(img, dtype=np.uint8))
        Labels.append(i)
    Labels = np.asarray(Labels, dtype=np.int32)
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(np.asarray(Data), np.asarray(Labels))
    model.write( "/home/gigachany/CODE/model/" + name)
    print("Complete [" + name + "]")


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
        file_name_path = '/home/gigachany/CODE/GiGAChany/OutImage/images.jpg'
        cv2.imwrite(file_name_path, face)
        model = cv2.face.LBPHFaceRecognizer_create()
        model.read("/home/gigachany/CODE/model/"+ModelName[number])
        result = model.predict(face)
        if result[1] < 500 :
            confidence = int(100 * (1 - (result[1]) / 500))
        return confidence
    except:
        print("Face Not Found")
        pass 

def Checker_Output(A, B):
    if A > B : return str(A + '^female')
    
    elif A < B : return str(B + '^male')
    else : return str('0^not')

def Server():
    TCP_IP = '10.10.20.54'
    TCP_PORT = 9097
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(True)
    s.accept()
    img = open("/home/gigachany/CODE/GiGAChany/SendImage/images.jpg","wb")
    data = s.recv(1024)
    img.write(data)
    img.close()
    print("이미지 저장 완료")
    s.close()

if __name__ == "__main__":
    Server();
    # path = '/home/gigachany/CODE/GiGAChany/SendImage/images.jpg'
    # image = cv2.imread(path)
    # print("Wait..")
    # Checker_Output(Gender_Checker(image, 0), Gender_Checker(image, 1))

