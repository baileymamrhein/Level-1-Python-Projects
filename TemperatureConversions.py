#Temperature conversions

getInput = input("Do you want to convert Farenheit to Celsius?")

if getInput=="yes":
        getNumber = input("Please enter a numerical value: ")
        # convert input from str to int
        getNumber = int(getNumber)
        # the formula to convert celsius to farenheit is x-32 * (5/9)
        convertedNumber=(round((getNumber-32) * (5/9)))

        # string the output together
        temperature = " degrees farenheit is " + str(convertedNumber) + " degrees in celsius."
        print(str(getNumber) + temperature)
        input("Press 'enter' to exit.")
        exit

if getInput=="no":
        getNumber = input("Please enter a numerical value: ")
        # convert input from str to int
        getNumber = int(getNumber)
        # the formula to convert celsius to farenheit is (9/5) + 32
        convertedNumber=(round((getNumber*(9/5))+32))

        # string the output together
        temperature = " degrees celsius is " + str(convertedNumber) + " degrees in farenheit."
        print(str(getNumber) + temperature)
        input("Press 'enter' to exit.")
        exit
else:
    print("Sorry, please answer yes or no!")
    input("Press 'enter' to exit and try again.")
