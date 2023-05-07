from miningFunctions import *
import keyboard
import os

def main():
    # begin program
    while True:
        # prompt User
        print("What would you like to do?\n" \
            + "(1) Craft then Sell\n" \
            + "(2) Craft\n" \
            + "(3) Sell\n" \
            + "(4) Idle\n"
            + "(5) Exit")
        val = input(": ")

        # check User Input, run
        match val:
            case '1':
                autoCraft() # craft script
                dx.press('i') # open inventory
                autoSell(1) # sell script
                
            case '2':
                autoCraft() # craft script

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
