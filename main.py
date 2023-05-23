from miningFunctions import *
import keyboard
import os

def main(): 
    # begin program
    size = auto.size()
    width = size[0]
    height = size[1]

    while True:
        # prompt User
        print("What would you like to do?\n" \
            + "(1) Full Automation"
            + "(2) Craft then Sell\n" \
            + "(3) Craft\n" \
            + "(4) Sell\n" \
            + "(5) Idle\n"
            + "(6) Exit")
        val = input(": ")

        # check User Input, run
        match val:
            case '1':
                break

            case '2':
                autoCraft(width, height) # craft script
                dx.press('i') # open inventory
                autoSell(1) # sell script
                
            case '2':
                autoCraft(width, height) # craft script

            case '3':
                autoSell(5) # sell script

            case '4':
                idleUntilAfk() # idle script
                exitAfk() # exit afk
                chooseMiningJob() # pick job

            case _:
                break # exit loop

        time.sleep(2)
        os.system('cls') # clear terminal

# initialize main function
if __name__ == "__main__":
    main()
