import subprocess
import keyboard
import time
import pyautogui
import schedule

url = 'https://jamboard.google.com/u/1/d/13O3UdEf-u_0_ulbVafXtZtgTRwfyrHr65oN1XmXfpcI/viewer?f=6'

oddorevenweek = False
def jamboard():
    global oddorevenweek
    subprocess.call(['C:\Program Files\Mozilla Firefox\\firefox.exe'])
    if oddorevenweek == True:
        time.sleep(3)
        keyboard.write(url)
        keyboard.press_and_release('enter')
        time.sleep(3)
        pyautogui.moveTo(350, 950)
        pyautogui.click(clicks=2)
        time.sleep(3)
        pyautogui.click(1125, 460)
        time.sleep(1)
        pyautogui.click(1125, 675)
        oddorevenweek = False
    elif oddorevenweek == False:
        time.sleep(3)
        keyboard.write(url) 
        keyboard.press_and_release('enter')
        time.sleep(3)
        pyautogui.moveTo(350, 950)
        pyautogui.click(clicks=2)
        time.sleep(3)
        pyautogui.click(1065, 460)
        time.sleep(1)
        pyautogui.click(1125, 675)
        oddorevenweek = True

jamboard()

schedule.every().thursday.at('13:00').do(jamboard)


while True:
    schedule.run_pending()
    time.sleep(1)

