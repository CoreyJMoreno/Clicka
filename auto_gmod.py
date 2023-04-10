import pyautogui as auto
import time

def autoCraft():
    # initialize variables
    exitX = 348
    exitY = 922

    # instruct user
    print("Go to crafting table and press e, now wait")
    time.sleep(3)

    # countdown until start
    countDownTimer(5)

    # move to craft button
    auto.moveTo(352, 437) 
    auto.click()

    # move to scroll area
    auto.moveTo(1620, 312) 
    auto.dragTo(1620, 900, button='left')

    # move to warhammer, click
    auto.moveTo(1326, 615)
    auto.click()

    # move to craft button
    auto.moveTo(1326, 942)

    # auto click
    craftClicker()

    # program done, exit screen
    print('Done, exiting')
    time.sleep(1)
    exitScreen(exitX, exitY)

def autoSell():
    # initialize variables
    colIndex = rowIndex = 1
    xStartPos = 1715
    yStartPos = 650
    shiftIndex = 125
    centerX = 950
    centerY = 555
    exitX = 1770
    exitY = 135

    # instruct user
    print("Press i, now wait")
    time.sleep(3)

    # countdown until start
    countDownTimer(5)

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
            innerLoopIndex += 1

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

def craftClicker():
    # initialize variables
    i = 0

    # loop until 150 clicks
    while i < 150:

        # click
        auto.click()

        # increment
        i += 1

        # print click number
        print('\r' + str(i), end='')

    # print endline
    print('\n', end='')

def exitScreen(x, y):
    # move to exit button, click
    auto.moveTo(x, y)
    auto.click()

def main():
    # begin program
    while True:
        # prompt User
        print("What would you like to do?")
        print("(1) Sell")
        print("(2) Craft")
        print("(3) Exit")
        val = input(": ")

        # check User Input, run
        if val == '1': #sell script
            autoSell()
            
        elif val == '2': #craft script
            autoCraft()

        elif val == '3': #exit loop
            break
            
        else: # error code
            print("Invalid Input, try again")

# initialize main function
if __name__ == "__main__":
    main()
