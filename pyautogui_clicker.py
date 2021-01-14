import pyautogui as p
from time import sleep
import keyboard
import mouse

sleep(3)
while True:
    mouse.click()
    if keyboard.is_pressed('q'):
        break
    else:
        continue
