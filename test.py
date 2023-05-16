import pyautogui as auto
import pydirectinput as dx
import numpy as np
from PIL import ImageGrab
import cv2
import time
from miningFunctions import *

def testAutoCraft(x, y):
    # instruct user
    print("Go to crafting table and press e, now wait")
    time.sleep(3)

    # countdown until start
    countDownTimer(5)

    # move to craft button
    auto.moveTo(int(x * .18333), int(y * 0.404629))
    auto.click()

    # move to scroll area
    auto.moveTo(int(x * 0.846), int(y * .288889))
    auto.dragTo(int(x * 0.846), int(y * 0.83333), button='left')

    # move to warhammer, click
    auto.moveTo(int(x * 0.6906), int(y * 0.569444))
    auto.click()

    # move to craft button
    auto.moveTo(int(x * 0.6906), int(y * 0.87222))

    # auto click
    craftClicker(88)

    # program done, exit screen
    print('Done, exiting')
    time.sleep(1)
    exitScreen(int(x * 0.18125), int(y * 0.8537))

def testAutoSell(timer, x, y):
    # initialize variables
    colIndex = rowIndex = 1
    xStartPos = int(x * 0.89323)
    yStartPos = int(y * 0.60185)
    xShiftIndex = int(x * 0.0651)
    yShiftIndex = int(y * 0.1157)
    centerX = int(x * 0.49479)
    centerY = int(y * 0.513889)
    exitX = int(x * 0.921875)
    exitY = int(y * 0.125)
    sellShift = int(y * 0.060185)

    # instruct user if chosen manually
    if timer == 5:
        print("Press i, now wait")
    time.sleep(1)

    # countdown until start
    countDownTimer(timer)

    while rowIndex <= 4:
        while colIndex <= 11:
            # move to first item in row
            auto.moveTo(xStartPos, yStartPos)
            auto.click()

            # move to sell button
            auto.moveRel(5, 150)
            auto.click()

            # switch item count from 1 to 2
            tchangeToTwo(centerX, centerY, sellShift)
            
            # shift mouse to next item
            xStartPos -= xShiftIndex

            # increment
            colIndex += 1

        # reset starting index
        xStartPos = 1715

        # shift row up 1
        yStartPos -= yShiftIndex

        # reset column counter
        colIndex = 1

        # increment row counter
        rowIndex += 1

    # Program done, exit screen
    print('Done, Exiting')
    time.sleep(1)
    exitScreen(exitX, exitY)

def tchangeToTwo(x, y, s):
    # move to input box
    auto.moveTo(x, y)
    auto.click(x, y)

    # delete 1, replace with 2
    auto.press('backspace')
    auto.press('2')

    # move to sell button
    auto.moveTo(x, y + s)
    auto.click()

# size = auto.size()
# testAutoSell(5, size[0], size[1])

def moveCheck():
    auto.moveRel(100, 0, 5)

time.sleep(4)
moveCheck()
