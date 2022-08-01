#exceptions allows to control the program in case of some error

# a= 10+"5"  (type error)
# import xxx (module not found error)
# b= c (name error)
# f=open('something.xyz') (file not found error)
# a=[1,2,3] a.remove(4)  (value error)
# a[4] (index error)
# my_dict = {'name':'max}   mydict['age']    (key error)
# assert not true   (assertion error)

# raise keyword is used to raise an exception



i =int(input("enter a value ")) 
if i<0:
    raise Exception("Value less than zero")
else:
    print("all good")

assert(i>0), "input is negative"


# to handle an exception , use try and except block as below

try:
    a=10/0
except Exception as e:
    print(e)
else:
    print("no exception")
finally:
    print("this will run anyways")


# creating your own exceptions

class ValueTooHighError(Exception):
    def __inti__(self,message,value):
        self.message = message
        self.value = value

def test(x):
    if x>30:
        raise ValueTooHighError("valu is mor than 30", x)
my_val = 50
try:
    test(my_val)
except ValueTooHighError as e:
    print(e)
