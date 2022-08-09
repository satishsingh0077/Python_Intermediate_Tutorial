# Generator : These are functions that returns object which can be iterated over.
# It iterates over it only once 
# They are memory effecient
# has same syntax as a function but instead of return, it has yield


def my_generator():
    yield 1
    yield 2
    yield 3

# creating the generatir object
# since one object is iterated over only once, we are creating multiple objects dor demostration
g = my_generator()
gen  = my_generator()

# can be iterated over
for i in g:
    print(i)


# can also be retrieved through next
# the concept is the execution will happen till the yield is reached and the value gets returned. For the next, it starts from there till next yield

val = next(gen)
print(val) # will give 1
val = next(gen)
print(val) # will give 2
val = next(gen)
print(val) # will give 3
#val = next(gen)
#print(val) # will give StopIteration exception

# Practical case
def calc(a,b):
    sum = a+b
    yield sum
    diff = a-b
    yield diff
    mul = a*b
    yield mul

#creating the object
c = calc(10,2)

s = next(c)
print("s = ",s)

d = next(c)
print("d = ",d)

m = next(c)
print("m = ",m)

# generator object can be passed to a function
c1 = calc(155,39)
print(sorted(c1)) # this will print all the yield values in sorted form

# comparing the benefits of generator
# we are gonna compare the size of function and generator that does the same thing

def f_all_num2_n(num): #function
    nums  = []
    n = 0
    while n<num:
        nums.append(n)
        n+=1
    return nums

def g_all_num2_n(num): # generator
    n = 0
    while n<num:
        yield n
        n+=1

# comparing the size of function object and generator object

import sys

print("The size of function object is ", sys.getsizeof(f_all_num2_n(10000))) # The size of function object is  85176
print("The size of generator object is ", sys.getsizeof(g_all_num2_n(10000))) #The size of generator object is  104

# the sizes are in bytes. The difference is evedient. Thus generators are memory effecient
# also in generator we dont have to store the value in list and we dont need to wait for the entire operation to finish.

# fibonachi with generator

def fibo(num):
    first, second  = 0,1
    n = 0
    while n < num:
        if n == 0:
            yield first
            n = n+1
        if n == 1:
            yield second
            n = n+1
            first, second  = second, first+second
        else:
            yield second
            n = n+1
            first, second  = second, first+second

fib  = fibo (10)
for val in fib:
    print(val, end=" ")

print()        
# generator expression
# this is similar to list comprehension
my_gen  = (i for i in range(100) if i%2 == 0)
print(type(my_gen)) #<class 'generator'>

# list comprehension
my_list  = [i for i in range(100) if i%2 == 0]
print(type(my_list)) #<class 'list'>

# generator object can be converted to a list
converted = list(my_gen)
print(converted)

# comparing the size again
print("generator size = ", sys.getsizeof(my_gen)) #generator size =  104
print("list size = ", sys.getsizeof(my_list)) #list size =  472