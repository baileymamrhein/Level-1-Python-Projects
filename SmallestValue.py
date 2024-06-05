##Biggest to smallest: practicing min/max

def getSmallest(numbers):
    if len(numbers) == 0:
        return None
    # smallest variable tracks the smallest value in the parameter so far
    # [0] is the first value
    smallest = numbers[0]

    # loop over all values in [] to find smallest. If new number is smaller
    # than current value, make new value smallest
    if number < smallest:
        smallest = number
        return smallest
    
    # check with asserts
    assert getSmallest ([1,2,3]) == 1
    assert getSmallest ([3, 7, 2]) == 2