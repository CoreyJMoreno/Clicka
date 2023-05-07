import pyautogui as auto
import pydirectinput as dx
import numpy as np
from PIL import ImageGrab
import cv2
import time
from mss import mss

bounding_box = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

screen = mss()

while True:
    screen_out = screen.grab(bounding_box)
    cv2.imshow('output', np.array(screen_out))

    if(cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break

# last_time = time.time()
# while True:
#     printscreen_pil = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
#     # print('Loop took {} seconds'.format(time.time()-last_time))
#     last_time = time.time()
#     cv2.imshow('window', cv2.cvtColor(np.array(printscreen_pil), cv2.COLOR_BGR2RGB))
#     if(cv2.waitKey(25) & 0xFF == ord('q')):
#         cv2.destroyAllWindows()
#         break