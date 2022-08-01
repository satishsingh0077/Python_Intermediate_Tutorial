# returning multiple values from a function
# just by using comma, 
# python returns them as tuple

def calculation(x,y):
    return x+y, x-y,x*y,x/y


value = calculation(10,2)
print(value)
print(type(value))