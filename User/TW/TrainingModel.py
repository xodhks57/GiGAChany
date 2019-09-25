from os import listdir as ld
from os.path import isfile, join 
import cv2
import numpy as np

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
    model.write(name)
    print("Complete [" + name + "]")

if __name__ == "__main__":
    path1 = '/home/gigachany/CODE/GiGAChany/Data/data_female/'
    path2 = '/home/gigachany/CODE/GiGAChany/Data/data_male/'
    file1 = [f for f in ld(path1) if isfile(join(path1, f))]
    file2 = [f for f in ld(path2) if isfile(join(path2, f))]
    Trainer("human_female", path1, file1)
    Trainer("human_male", path1, file1)