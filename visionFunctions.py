import pyautogui as auto
import pydirectinput as dx
import numpy as np
import cv2 as cv
import time
from windowCapture import windowCapture
from miningFunctions import exitAfk

# time.sleep(3)
def visionHelper(haystackImg, needlePath, debug):
    # haystackImg = cv.imread(haystack_path, cv.IMREAD_UNCHANGED)
    needleImg = cv.imread(needlePath, cv.IMREAD_UNCHANGED)

    result = cv.matchTemplate(haystackImg, needleImg, cv.TM_CCOEFF_NORMED)

    minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(result)

    threshhold = 0.5

    if maxVal >= threshhold:
        needleW = needleImg.shape[1]
        needleH = needleImg.shape[0]
        topLeft = maxLoc
        bottomRight = (topLeft[0] + needleW, topLeft[1] + needleH)
        cv.rectangle(haystackImg, topLeft, bottomRight, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
        return True

    if debug == True:
        cv.imshow('Result', haystackImg)

# main actions
def checkForFullOrAFK(x, y, debug):
    while(True):
        screenshot = windowCapture(x, y)
        errorResult = visionHelper(screenshot, 'error_needle.jpg', debug)
        afkResult = visionHelper(screenshot, 'afk_screen.jpg', debug)
        if errorResult == True:
            dx.click()
            time.sleep(2)
            break
        
        if afkResult == True:
            time.sleep(2)
            exitAfk()
            break

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

checkForFullOrAFK(1920, 1080, True)
