# Ordinal and cardinal

# Challenge description: write a function that takes any integer and returns the ordinal 

n = input("Please enter a number: ")
numStr = n[-2:]

## 'in' checks to see if the same values are stored in memory. == checks to see if the values are equal
if numStr in ('11', '12', '13'):
    print(numStr + "th")
elif int(n) % 10 == 1:
    print (n + "st")
elif int(n) % 10 == 2:
    print (n + "nd")
elif int(n) % 10 == 3:
    print (n + "rd")
else:
    print(n + "th")
