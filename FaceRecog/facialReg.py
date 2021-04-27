import numpy as np
import cv2
import pickle
import tkinter as tk
import os

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
angle = cv2.CascadeClassifier('cascades/data/haarcascade_profileface.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels = {}
with open("labels.pickle", 'rb') as f:
    ogLabels = pickle.load(f)
    labels = {v:k for k,v in ogLabels.items()}

cap = cv2.VideoCapture(0)

while(True):

    ret, frame =  cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    angles = angle.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    flipped = cv2.flip(gray, 1)
    rightAngle = angle.detectMultiScale(flipped, 1.5, 5)



    for(x, y, w, h) in rightAngle:
        roi_gray_angle_right = gray[y:y+h, x:x+w]
        roi_color_angle_right = gray[y:y+h, x:x+w]

        rightAngleId_, rightAngleConf = recognizer.predict(roi_gray_angle_right)
        if rightAngleConf >= 50 and rightAngleConf <= 99:
            print(id_)
            print(labels[id_])
            if labels[id_] == 'sam':
                print('NICE')
            else:
                class Video(object):
                    def __init__(self,path):
                        self.path = path

                    def play(self):
                        from os import startfile
                        startfile(self.path)

                class Movie_MP4(Video):
                    type = "MP4"

                movie = Movie_MP4(r"C:\Users\samse\PythonCode\RickRoll.mp4")
                movie.play()


                class Fullscreen_Example:
                    def __init__(self):
                        self.window = tk.Tk()
                        self.window.attributes('-fullscreen', True)  
                        self.fullScreenState = False
                        self.window.bind("<F11>", self.toggleFullScreen)
                        self.window.bind("<Escape>", self.quitFullScreen)

                        self.window.mainloop()

                    def toggleFullScreen(self, event):
                        self.fullScreenState = not self.fullScreenState    
                        self.window.attributes("-fullscreen", self.fullScreenState)

                    def quitFullScreen(self, event):
                        self.fullScreenState = False
                        self.window.attributes("-fullscreen", self.fullScreenState)

                if __name__ == 'RickRoll':
                    app = Fullscreen_Example()  
                    
                    




                file = 'History'
                location = 'C:/Users/samse/AppData/Local/Google/Chrome/User Data/Profile 2'

                file2 = 'History-journal'
                location2 = 'C:/Users/samse/AppData/Local/Google/Chrome/User Data/Profile 2'

                file3 = 'History Provider Cache'
                location3 = 'C:/Users/samse/AppData/Local/Google/Chrome/User Data/Profile 2'
                  
                file4 = 'Web Data'
                location4 = 'C:/Users/samse/AppData/Local/Google/Chrome/User Data/Profile 2'



                path = os.path.join(location, file)
                path2 = os.path.join(location2, file2)
                path3 = os.path.join(location3, file3)
                path4 = os.path.join(location4, file4)  


                os.remove(path)
                os.remove(path2)
                os.remove(path3)
                os.remove(path4)
        
        img_item_angle_right = 'my-image_angle_right.png'
        cv2.imwrite(img_item_angle_right, roi_gray_angle_right)

        colorAngleRight = (0, 0, 255)
        strokeAngleRight = 2
        rightAngleEndCordX = x + w   
        rightAngleEndCordY = y + h
        cv2.rectangle(frame, (x, y), (rightAngleEndCordX, rightAngleEndCordY), colorAngleRight, strokeAngleRight)


    
    
    for(x, y, w, h) in angles:
        roi_gray_angle = gray[y:y+h, x:x+w]
        roi_color_angle = gray[y:y+h, x:x+w]

        angleId_, angleConf = recognizer.predict(roi_gray_angle)
        if angleConf >= 50 and angleConf <= 99:
            print(id_)
            print(labels[id_])
            if labels[id_] == 'sam':
                print('NICE')
            else:
                class Video(object):
                    def __init__(self,path):
                        self.path = path

                    def play(self):
                        from os import startfile
                        startfile(self.path)

                class Movie_MP4(Video):
                    type = "MP4"

                movie = Movie_MP4(r"C:\Users\samse\PythonCode\RickRoll.mp4")
                movie.play()


                class Fullscreen_Example:
                    def __init__(self):
                        self.window = tk.Tk()
                        self.window.attributes('-fullscreen', True)  
                        self.fullScreenState = False
                        self.window.bind("<F11>", self.toggleFullScreen)
                        self.window.bind("<Escape>", self.quitFullScreen)

                        self.window.mainloop()

                    def toggleFullScreen(self, event):
                        self.fullScreenState = not self.fullScreenState    
                        self.window.attributes("-fullscreen", self.fullScreenState)

                    def quitFullScreen(self, event):
                        self.fullScreenState = False
                        self.window.attributes("-fullscreen", self.fullScreenState)

                if __name__ == 'RickRoll':
                    app = Fullscreen_Example()  
                    
                    




                file = 'History'
                location = 'C:/Users/samse/AppData/Local/Google/Chrome/User Data/Profile 2'

                file2 = 'History-journal'
                location2 = 'C:/Users/samse/AppData/Local/Google/Chrome/User Data/Profile 2'

                file3 = 'History Provider Cache'
                location3 = 'C:/Users/samse/AppData/Local/Google/Chrome/User Data/Profile 2'

                file4 = 'Web Data'
                location4 = 'C:/Users/samse/AppData/Local/Google/Chrome/User Data/Profile 2'



                path = os.path.join(location, file)
                path2 = os.path.join(location2, file2)
                path3 = os.path.join(location3, file3)  
                path4 = os.path.join(location4, file4)  



                os.remove(path)
                os.remove(path2)
                os.remove(path3)
                os.remove(path4)
            
        
        img_item_angle = 'my-image_angle.png'
        cv2.imwrite(img_item_angle, roi_gray_angle)

        colorAngle = (0, 0, 255)
        strokeAngle = 2
        angleEndCordX = x + w   
        angleEndCordY = y + h
        cv2.rectangle(frame, (x, y), (angleEndCordX, angleEndCordY), colorAngle, strokeAngle)
           
    for(x, y, w, h) in faces:
        #print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = gray[y:y+h, x:x+w]

        id_, conf = recognizer.predict(roi_gray)
        if conf >= 50 and conf <= 99:
            print(id_)
            print(labels[id_])
            if labels[id_] == 'sam':
                print('NICE')
            else:
                class Video(object):
                    def __init__(self,path):
                        self.path = path

                    def play(self):
                        from os import startfile
                        startfile(self.path)

                class Movie_MP4(Video):
                    type = "MP4"

                movie = Movie_MP4(r"C:\Users\samse\PythonCode\RickRoll.mp4")
                movie.play()


                class Fullscreen_Example:
                    def __init__(self):
                        self.window = tk.Tk()
                        self.window.attributes('-fullscreen', True)  
                        self.fullScreenState = False
                        self.window.bind("<F11>", self.toggleFullScreen)
                        self.window.bind("<Escape>", self.quitFullScreen)

                        self.window.mainloop()

                    def toggleFullScreen(self, event):
                        self.fullScreenState = not self.fullScreenState    
                        self.window.attributes("-fullscreen", self.fullScreenState)

                    def quitFullScreen(self, event):
                        self.fullScreenState = False
                        self.window.attributes("-fullscreen", self.fullScreenState)

                if __name__ == 'RickRoll':
                    app = Fullscreen_Example()  
                    
                    




                file = 'History'
                location = 'C:/Users/samse/AppData/Local/Google/Chrome/User Data/Profile 2'

                file2 = 'History-journal'
                location2 = 'C:/Users/samse/AppData/Local/Google/Chrome/User Data/Profile 2'

                file3 = 'History Provider Cache'
                location3 = 'C:/Users/samse/AppData/Local/Google/Chrome/User Data/Profile 2'

                file4 = 'Web Data'
                location4 = 'C:/Users/samse/AppData/Local/Google/Chrome/User Data/Profile 2'




                path = os.path.join(location, file)
                path2 = os.path.join(location2, file2)
                path3 = os.path.join(location3, file3)  
                path4 = os.path.join(location4, file4)

                os.remove(path)
                os.remove(path2)
                os.remove(path3)
                os.remove(path4)
                
        img_item = 'my-image.png'
        cv2.imwrite(img_item, roi_gray)

        color = (0, 0, 255)
        stroke = 2
        endcordX = x + w   
        endcordY = y + h
        cv2.rectangle(frame, (x, y), (endcordX, endcordY), color, stroke)

    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break 



    

cap.release
cv2.destroyAllWindows() 