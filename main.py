from functions import *
# from resolutionClass import *

def main():
    # begin program
    dimensions = sizeUp()
    print(dimensions)

    r = chooseDimension(dimensions)
    print(r)

    while True:
        # prompt User
        print("What would you like to do?")
        print("(1) Sell")
        print("(2) Craft")
        print("(3) Exit")
        val = input(": ")

        # check User Input, run
        match val:
            case '1':
                autoSell(dimensions) #sell script
            case '2':
                autoCraft(dimensions) #craft script
            case '3':
                break #exit loop
            case _:
                print("Invalid Input, try again") # error code

# initialize main function
if __name__ == "__main__":
    main()
