# The classic FizzBuzz prompt: write a function that repsonds with the following:
# Prints "fizzbuzz" if n is divisible by 3 and 5
# Prints "fizz" if n is divisible by 3
# Prints "buzz" if n is divisible by 5
# Prints the number if the number is not divisible by 3 or 5

n = input("Please enter a number: ")
upTo = int(n)

def fizzbuzz(upTo):
    for upTo in range(1, upTo+1):
        if upTo % 15==0:
            print("fizzbuzz ")
        elif upTo % 5==0:
            print("buzz ")
        elif upTo % 3==0:
            print("fizz")
        else:
            print(upTo)
fizzbuzz(upTo)