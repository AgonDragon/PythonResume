import pyautogui
import time
from mss import mss

start_x = 790
start_y = 600

bbox = (start_x, start_y, start_x +451, start_y + 1)
cords_x = [0, 150, 300, 450]

def start():
    with mss() as sct:
        while True:
            img = sct.grab(bbox)
            for cord in cords_x:
                if img.pixel(cord, 0)[0] <100:
                    pyautogui.click(start_x + cord, start_y)
                    break

time.sleep(5)
start()