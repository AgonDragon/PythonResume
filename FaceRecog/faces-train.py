import os
import cv2
from PIL import Image  
import numpy as np
import pickle

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

currentId = 0
labelIds = {}

xTrain = []
yLabels = []

for root, dirs, files, in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(' ', '-').lower()
            #print(label, path)
            if not label in labelIds:
                labelIds[label] = currentId
                currentId += 1

            id_ = labelIds[label]
            #print(labelIds)
            #yLabels.append(label)
            #xTrain.append(path)
            pilImage = Image.open(path).convert("L")
            imageArray = np.array(pilImage, "uint8")
            #print(imageArray)
            faces = face_cascade.detectMultiScale(imageArray, scaleFactor=1.5, minNeighbors=5)  
            for(x, y, w, h) in faces:
                roi = imageArray[y:y+h, x:x+w]
                xTrain.append(roi)
                yLabels.append(id_)

#print(yLabels)
#print(xTrain)


with open("labels.pickle", 'wb') as f:
    pickle.dump(labelIds, f)


for x in range(0, 301):   
    recognizer.train(xTrain, np.array(yLabels))
    recognizer.save("trainer.yml")
    print(x)
