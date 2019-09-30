from PIL import Image
import os,glob
import numpy as np
from sklearn.model_selection import train_test_split
import cv2
from sklearn.model_selection import train_test_split
from PIL import Image
import os, glob
from os import listdir
from os.path import isfile, join
import numpy as np
import cv2


#분류대상 카테고리
root_dir="/home/iot/images/"
categories=["happy","angry","scared","sad","soso","satisfied"]
nb_classes=len(categories)
image_size=60

#얼굴 인식용 xml파일
face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
###################################얼굴자르기########################
raw_image_path="/home/iot/images/"

#전체 사진에서 얼굴 부위만 잘라 리턴
def face_extractor(img):
    #흑백처리
    try:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #얼굴 찾기
        faces = face_classifier.detectMultiScale(gray,1.3,5)
        #찾은 얼굴이 없으면 None으로 리턴
        if faces is():
            return None
        #얼굴이 있으면
        for(x,y,w,h) in faces:
        #해당 얼굴 크기만큼 cropped_face에 잘라 넣기
            cropped_face = img[y:y+h, x:x+w]
        #cropped_face 리턴
        return cropped_face
    except:
        pass




#자른 얼굴을 저장할 곳
face_path="/home/iot/KH/face/"

#raw_image_path내의 파일리스트 얻기
categories_count=-1
for(path,dirs,files) in os.walk(raw_image_path):  #os.walk는 [주소], [하위디렉토리,,,], [하위파일,,]구조
    subfile=[f for f in listdir(path) if isfile(join(path,f))]
    categories_count+=1
    count=0
    #파일 갯수만큼 루프
    for i, files in enumerate(subfile):
        #파일이름 생성
        image_path=path+subfile[i]
        #이미지 불러오기
        images=cv2.imread(image_path)
        if face_extractor(images) is not None:
            count+=1
            #얼굴 이미지 크기를 조정
            face=cv2.resize(face_extractor(images),(200,200))
            #조정된 이미지를 흑백으로 변환
            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
            #face폴더에 jpg파일로 저장
            file_name_path=face_path+categories[categories_count]+"/"+str(count)+'.jpg'
            cv2.imwrite(file_name_path,face)
        else:
            print("Face not Found")
            pass

############################################얼굴자르기 끝#################################
######################################자른 얼굴을 이용해 이미지,레이블 형태로 변환#############


#얼굴 이미지 데이터 읽어 들이기
X=[]#이미지 데이터
Y=[]#레이블 데이터


for idx,cat in enumerate(categories):
    image_dir=face_path+"/"+cat
    files =glob.glob(image_dir+"/*.jpg")#glob~ 매개변수의 확장자에 따라 [~.jpg, ~.jpg,~.jpg]꼴로바꿔줌
    print("---",cat,"처리 중")
    print(files)#######################
    for i, f in enumerate(files):

        img=Image.open(f)
        img=img.convert("RGB")#색상모드변경
        img=img.resize((image_size,image_size))#이미지 크기 변경
        data = np.asarray(img)
        X.append(data)
        Y.append(cat)

X=np.array(X)
Y=np.array(Y)
print("X=",X,"\n")
print("Y=",Y,"\n")
#학습전용데이터와 텍스트 전용데이터 분류하기
X_train,X_test,Y_train,Y_test=train_test_split(X,Y)
xy=(X_train,X_test,Y_train,Y_test)
np.save("./emotions.npy",xy)
print("ok",len(Y))

