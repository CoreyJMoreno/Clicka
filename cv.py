import pyautogui as auto
import pydirectinput as dx
import numpy as np
from PIL import ImageGrab
import cv2 as cv
import time
from mss import mss

# time.sleep(3)

haystackImg = cv.imread('haystack3.jpg', cv.IMREAD_UNCHANGED)
needleImg = cv.imread('needle.jpg', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(haystackImg, needleImg, cv.TM_CCOEFF_NORMED)

minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(result)
print('best top left position: %s' % str(maxLoc))
print('best match confidence: %s' % maxVal)

threshhold = 0.3
if maxVal >= threshhold:
    print('found')

    needleW = needleImg.shape[1]
    needleH = needleImg.shape[0]

    topLeft = maxLoc
    bottomRight = (topLeft[0] + needleW, topLeft[1] + needleH)

    cv.rectangle(haystackImg, topLeft, bottomRight, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

    cv.imshow('Result', haystackImg)
    cv.waitKey()

else:
    print('not found')

time.sleep(5)
auto.moveTo(1112, 78)