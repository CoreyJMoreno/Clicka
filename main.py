from functions import *

def main():
    # begin program
    while True:
        # prompt User
        print("What would you like to do?")
        print("(1) Craft then Sell")
        print("(2) Craft")
        print("(3) Sell")
        print("(4) Exit")
        val = input(": ")

        # check User Input, run
        match val:
            case '1':
                autoCraft()
                autoSell()
            case '2':
                autoCraft() #craft script
            case '3':
                autoSell() #sell script
            case '4':
                break #exit loop
            case _:
                print("Invalid Input, try again") # error code

# initialize main function
if __name__ == "__main__":
    main()
