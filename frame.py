import numpy as np
from PIL import ImageGrab
import cv2
import time

gameCoords = [456, 32, 892, 533]

screen=np.array(ImageGrab.grab(bbox=gameCoords))
screen=cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)

for i in range(1000):
    starttime=time.time()
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            if screen[y][x]<10:
                pass
    print("Frame took {} seconds for frame {}".format((time.time()-starttime),i))