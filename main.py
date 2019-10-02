import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click, queryMousePosition
import time
import keyboard

gameCoords = [456, 102, 892, 533]

def StartClicking(screen):
    global gameCoords
    for y1 in range(5, len(screen) - 5, 5):
        for i in range(4):
            w = gameCoords[2] - gameCoords[0]
            x = i * w / 4 + w / 8
            y = len(screen) - y1
            #print(screen[y][int(x)])
            #if screen[y][int(x)] < 40:
            if screen[y][int(x)] < 40:
                actualX = x + gameCoords[0]
                actualY = y + gameCoords[1]
                click(actualX, actualY)
                return
flag=True
while flag:
    if keyboard.is_pressed('r'):
        while True:
            if keyboard.is_pressed('1'):
                flag=False
                break
            mousePos = queryMousePosition()

            if gameCoords[2] > mousePos.x > gameCoords[0]:
                startTime = time.time()
                screen = np.array(ImageGrab.grab(bbox=gameCoords))
                screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                StartClicking(screen)
            else:
                if mousePos.x < 0:
                    while True:
                        mousePos = queryMousePosition()
                        if gameCoords[2] < mousePos.x:
                            break
