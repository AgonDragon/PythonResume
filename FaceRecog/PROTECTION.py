import os


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

import tkinter as tk

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
    app = Fullscreen_Example()  s




file = 'History'
location = 'C:/Users/samse/AppData/Local/Google/Chrome/User Data/Profile 2'

file2 = 'History-journal'
location2 = 'C:/Users/samse/AppData/Local/Google/Chrome/User Data/Profile 2'

file3 = 'History Provider Cache'
location3 = 'C:/Users/samse/AppData/Local/Google/Chrome/User Data/Profile 2'



path = os.path.join(location, file)
path2 = os.path.join(location2, file2)
path3 = os.path.join(location3, file3)  


os.remove(path)
os.remove(path2)
os.remove(path3)

