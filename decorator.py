#decorator: Function decorators and class decorators

# function decorators are functions that take another function as argument and extends its functioinality without explicitly modifying it.
# in plain text, it extends functionality of a function

# basic example without argument

def extend_hello(func): #this will take function as an argument
    def wrapper(): # a wrapper function is a function that wraps around another function
        print("Start function")
        func()
        print("Stop function")
    return wrapper # from extend_hello , we are returning a function

@extend_hello # this basically tells that when ever hello is called, call extend_hello and pass hella to it as argument
def hello(): # basic function that prints hello world. Now we wants to extend its functionality
    print("Hello World")

#x= extend_hello(hello)# this will retrn wrapper so x= wrapper
#x() # this is same as calling wrapper
# to eliminate the above syntax, we decorate the function. See line 15

# calling hello directly as it is decorated now. It will give the same result as above.
hello()

############################################################################################

print("**** Decorator with arguments ****")
# decorating functions that takes parameters
def add_decorator(func):
    def wrapper(*args, **kwargs): # the wrapper is taking generic arguments
        print("Below is the summation of the input")
        return_val = func(*args, **kwargs) # the egeneric aruments is being passed to the function.
        # since the function returns a value, we need to assign it to a variable and return it. As done above
        print("Done")
        return return_val # wrapper function is returning a value
    return wrapper

@add_decorator
def add_numbers(a,b):
    print("Summation...")# This will be executed before the result becuse the execution is happening inside wrapper and the sum is returned later
    return a+b

sum = add_numbers(10,20) # return value will be assigned to sum
print(sum)

# decorating a member method

class animal:
    def __init__(self,a,b):
        self.val1 = a
        self.val2 = b
    @add_decorator #decorating member method
    def animal_age(self):
        print("from animal class")
        return self.val1+self.val2

cat = animal(3,4)
age = cat.animal_age()
print(age)