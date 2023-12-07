#Even or odd?

# Practice creating/calling functions and using modulo operator
def calculator():
    getInput = input("Pick any number: ")
    global number 
    number = (round(int(getInput)))
    remainder = number%2

    if remainder==0:
        print((str(getInput)) + " divided by 2 has a reminder of " + (str(remainder)) + ", therefore it is even.")
        print("Press 'enter' to exit.")
    else:
        print((str(getInput)) + " divided by 2 has a remainder of " + (str(remainder)) + ", therefore it is odd.")
        print("Press 'enter' to exit.")

calculator()

