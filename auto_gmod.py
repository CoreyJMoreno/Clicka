import pyautogui as auto
import time

def autoCraft():
    exitX = 348
    exitY = 922

    print("Go to crafting table and press e, now wait")
    time.sleep(3)

    countDownTimer(5)

    auto.moveTo(352, 437) #move to craft button
    auto.click()

    auto.moveTo(1620, 312) #move to scroll area
    auto.dragTo(1620, 900, button='left')

    auto.moveTo(1326, 615)
    auto.click()

    auto.moveTo(1326, 942)

    craftClicker()

    print('Done, exiting')
    time.sleep(1)
    exitScreen(exitX, exitY)

def autoSell():
    innerLoopIndex = outerLoopIndex = 1
    xStartPos = 1715
    yStartPos = 650
    shiftIndex = 125
    centerX = 950
    centerY = 555
    exitX = 1770
    exitY = 135

    print("Press i, now wait")
    time.sleep(3)

    countDownTimer(5)

    while outerLoopIndex <= 4:
        while innerLoopIndex <= 11:
            auto.moveTo(xStartPos, yStartPos)
            auto.click()

            auto.moveRel(5, 150)
            auto.click()

            changeToTwo(centerX, centerY)
            
            xStartPos -= shiftIndex

            innerLoopIndex += 1

        xStartPos = 1715
        yStartPos -= shiftIndex
        innerLoopIndex = 1
        outerLoopIndex += 1

    print('Done, Exiting')
    time.sleep(1)
    exitScreen(exitX, exitY)

def changeToTwo(x, y):
    auto.moveTo(x, y)
    auto.click(x, y)
    auto.press('backspace')
    auto.press('2')
    auto.moveTo(x, y + 65)
    auto.click()

def countDownTimer(seconds):
    countDown = seconds
    while countDown >= 1: 
        print('\r' + str(countDown), end='')
        countDown -= 1
        time.sleep(1)
    print('\rStart')

def craftClicker():
    i = 0
    while i < 88:
        auto.click()
        i += 1
        print('\r' + str(i), end='')
    print('\n', end='')

def exitScreen(x, y):
    auto.moveTo(x, y)
    auto.click()

def main():

    while True:
        print("What would you like to do?")
        print("(1) Sell")
        print("(2) Craft")
        print("(3) Exit")
        val = input(": ")

        if val == '1': #sell script
            autoSell()
            
        elif val == '2': #craft script
            autoCraft()

        elif val == '3': #exit loop
            break
            
        else:
            print("Invalid Input, try again")

if __name__ == "__main__":
    main()
