# Praciting def, return, and assert

# Prompt: write four functions; area, perimeter, volume, and surface area and check them with
  # assert

def area(length, width):
    return length*width

def perimeter(length, width):
    return ((length+width)*2)

def volume(length, width, height):
    return (length*width*height)

def surfaceArea(length, width, height):
    return (((length*width)*2)+((length*height)*2)+((width*height)*2))

# Test with assert

assert area(10,10)==100
assert perimeter(5,8)==26
assert volume(5,8,10)==400
assert surfaceArea(5,8,10)==340
