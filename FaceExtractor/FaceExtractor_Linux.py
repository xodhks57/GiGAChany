import cv2
import os
import numpy as np

face_classifier = cv2.CascadeClassifier('/home/gigachany/anaconda3/envs/gigachany/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

def face_extractor(img):
    try : 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray,1.3, 5)
        if faces is ():
            return None 
        for (x, y, w, h) in faces:
            cropped_face = img[y:y + h, x:x + w]
        return cropped_face 
    except:
        pass  

def face_Data(name):
    img = cv2.imread(name)
    if face_extractor(img) is not None:
        face = cv2.resize(face_extractor(img), (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        file_name_path = '/home/gigachany/CODE/GiGAChany/data/data_male/m' + str(count) + '.jpg'
        cv2.imwrite(file_name_path, face)
        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Face Cropper', face)
    else:
        print("[" + name + "]" + " Face not Found")
    pass

if __name__ == "__main__":
    ImgList = os.listdir('/home/gigachany/CODE/GiGAChany/data/faces/')
    print(ImgList)
    count = 0
    while True:
        face_Data('/home/gigachany/CODE/GiGAChany/data/faces/'+ ImgList[count])
        count += 1
        if cv2.waitKey(1) == 13 or count == len(ImgList):
            break
    print('Colleting Samples Complete!!!')