import pyautogui as auto
import PySimpleGUI as gui
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

    promptButton = [
        [
        gui.Text("What would you like to do?", font=("Arial", 15)),
        gui.Button("Craft"),
        gui.Button("Sell")
        ],
        [
        gui.Text(key='-COUNTDOWN-')
        ]
    ]

    window = gui.Window("Auto GMOD", promptButton, margins=(200, 100))

    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED:
            break
        elif event == "Craft":
            autoCraft()
        elif event == "Sell":
            autoSell()
    window.close()

if __name__ == "__main__":
    main()
