#args = positional arguments. accpted in called function as tuples
#kwargs = keywords arguments accepted in called function as dictionary

def my_func(required, *args, **kwargs):
    print(required)
    print(args)
    print(kwargs)

# my_func() #this will throw error as it will it requires atleast one argument

#my_func("hello")
# since we are prining args and quargs and not passing them, we will get empty tuple and dictionary as output along with required

#my_func("hello", 1,2,"hi",3) # 1,2,"hi",3 are positional arguments so output will have then as tuples

my_func("hi", 1,2, key1="apple", key2="banana")# key1="apple", key2="banana" are keyword arguments 
