from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam
from keras.utils import np_utils
import numpy as np

#데이터 읽어들이기 (일단 느낌만)


#(X_train,Y_train),(X_test,Y_test)=data
X_train,X_test,Y_train,Y_test=np.load("./~.npy")


#데이터를 float32 자료형으로 변환하고 정규화

X_train= X_train.reshape(60000,784).astype('float32')
X_test= X_test.reshape(10000,784).astype('float')
X_train /=255
X_test/=255

#레이블 데이터를 6개의 표정 카테고리를 나타내는 배열로 변환하기
Y_train=np_utils.to_categorical(Y_train,6)
Y_test=np_utils.to_categorical(Y_test,6)


#모델 구조 정의
model=Sequential()
model.add(Dense(512,input_shape=(784,)))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(10))
model.add(Activation('softmax'))


#모델 구축하기
model.compile(
    loss='categorical_crossentropy',
    optimizer=Adam(),
    metrics=['accuracy'])
#데이터 훈련하기
hist=model.fit(X_train,Y_train)

#데이터 평가하기
score=model.evaluate(X_test,Y_test,verbose=1)
print('loss=',score[0])
print('accuracy=',score[1])