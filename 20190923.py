import cv2
import os
import numpy as np

face_classifier = cv2.CascadeClassifier('/home/gigachany/anaconda3/envs/gigachany/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

def face_extractor(img):    # 사진 얼굴 추출 리턴
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     # 흑백처리
    faces = face_classifier.detectMultiScale(gray,1.3, 5)     # 얼굴 찾기
    if faces is ():
        return None     # 찾은 얼굴이 없으면 None으로 리턴
    for (x, y, w, h) in faces:     # 얼굴들이 있으면
        cropped_face = img[y:y + h, x:x + w]
    return cropped_face     # cropped_face 리턴

def face_Data(name):
    # 카메라로 부터 사진 1장 얻기
    img = cv2.imread(name)
    # 얼굴 감지 하여 얼굴만 가져오기

    if face_extractor(img) is not None:
        # 얼굴 이미지 크기를 200x200으로 조정
        face = cv2.resize(face_extractor(img), (200, 200))
        # 조정된 이미지를 흑백으로 변환
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        # faces폴더에 jpg파일로 저장
        # ex > faces/user0.jpg   faces/user1.jpg ....
        file_name_path = 'faces/' + str(count) + '.jpg'
        cv2.imwrite(file_name_path, face)

        # 화면에 얼굴과 현재 저장 개수 표시
        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Face Cropper', face)
    else:
        print("Face not Found")
    pass

ImgList = os.listdir('./data')
print(ImgList)
count = 0 # 저장할 이미지 카운트 변수
while True:
    face_Data('./data/'+ ImgList[count])
    count += 1
    if cv2.waitKey(1) == 13 or count == len(ImgList):
        break
    print('Colleting Samples Complete!!!')
