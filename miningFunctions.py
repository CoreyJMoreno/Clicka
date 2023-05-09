# modules
import pyautogui as auto
import pydirectinput as dx
import numpy as np
from PIL import ImageGrab
import cv2
import time

def autoCraft(x, y):
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

def autoSell(timer):
    # initialize variables
    colIndex = rowIndex = 1
    xStartPos = 1715
    yStartPos = 650
    shiftIndex = 125
    centerX = 950
    centerY = 555
    exitX = 1770
    exitY = 135

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
            changeToTwo(centerX, centerY)
            
            # shift mouse to next item
            xStartPos -= shiftIndex

            # increment
            colIndex += 1

        # reset starting index
        xStartPos = 1715

        # shift row up 1
        yStartPos -= shiftIndex

        # reset column counter
        colIndex = 1

        # increment row counter
        rowIndex += 1

    # Program done, exit screen
    print('Done, Exiting')
    time.sleep(1)
    exitScreen(exitX, exitY)

def changeToTwo(x, y):
    # move to input box
    auto.moveTo(x, y)
    auto.click(x, y)

    # delete 1, replace with 2
    auto.press('backspace')
    auto.press('2')

    # move to sell button
    auto.moveTo(x, y + 65)
    auto.click()

def chooseMiningJob():
    dx.press('f4') # open jobs
    auto.moveTo(430, 380) # move to jobs
    auto.click()
    auto.moveTo(730, 300) # move to citizens
    auto.click()
    auto.moveTo(730, 375) # move to miner
    auto.click()
    time.sleep(.5)
    auto.moveTo(1180, 880) # confirm
    auto.click()
    time.sleep(1.5)
    dx.press('3') # get pick
    auto.click()

def countDownTimer(seconds):
    # initialize variables
    countDown = seconds

    # loop until timer is 1
    while countDown >= 1: 
        # print countdown
        print('\r' + str(countDown), end='')

        # decrement
        countDown -= 1

        # sleep for timer effect
        time.sleep(1)

    # tell user program has started
    print('\rStart')

def craftClicker(clicks):
    # initialize variables
    index = 0

    while index < clicks:

        # click
        auto.click()
        time.sleep(.15)

        # increment
        index += 1

        # print click number
        print('\r' + str(index), end='')

    # print endline
    print('\n', end='')

def exitAfk():
    # exit afk mode
    dx.press('y')
    auto.press('/')
    auto.press('a')
    auto.press('f')
    auto.press('k')
    auto.press('enter')
    time.sleep(2)

def exitScreen(x, y):
    # move to exit button, click
    auto.moveTo(x, y)
    auto.click()

def idleUntilAfk():
    # initialize time
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    # check if current time is server restart time
    while current_time != "10:00:00":
        # update time
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print('\r' + "Time: " + str(current_time), end='')
        continue

    print("\nexit at " + current_time)
