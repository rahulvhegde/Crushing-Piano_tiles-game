import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click, queryMousePosition
import time
import numpy as np
from PIL import Image
import keyboard
import pyautogui as p
from pynput.mouse import Button, Controller
mouse = Controller()


gameCoords = [456, 102, 892, 533]

score = 0
previousLane = -1

# while True:
#     if keyboard.is_pressed('l'):
#         break

while True:
    if keyboard.is_pressed('q'):
        break
    startTime = time.time()
    screen = np.array(ImageGrab.grab(bbox=gameCoords))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    print(len(screen))
    #img = Image.fromarray(screen)
    #img.show()
    #time.sleep(3)

    
    