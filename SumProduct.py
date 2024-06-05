# Sum & Product

def calculateSum(numbers):
    if numbers == 0:
        return None
    
    ## start at 0
    result = 0
    for number in numbers:
        result += number
    return result

def calculateProduct(numbers):
    if numbers == 0:
        return 1
    
    result = 1
    for number in numbers:
        result *= number
    return result

#test with asserts
assert calculateSum([]) == 0
assert calculateSum([3,20,22,4]) == 49
assert calculateProduct([]) == 1
assert calculateProduct([2,4,6,8]) == 384