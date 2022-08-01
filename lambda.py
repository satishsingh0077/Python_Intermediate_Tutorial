# lambda functions: one line anonymous functuions 
# syntax   lambda argument:expression

# simple lambda that takes x and y as arguments and retun the sum
add_val = lambda x,y: x+y
print(add_val(10,20))

# lambda is used in places where it can be pased as function to another higher function of at places where the dunction is used only once
# example we are sorting a list which has pair of values
data_2d = [(1,2),(7,-1),(4,5),(2,-4),(1,3)]
sorteded_data = sorted(data_2d)  # by default is sorts based on first element
print(data_2d)
print(sorteded_data)

# sorting based on 2nd element
sorted_data_2nd = sorted(data_2d, key = lambda x:x[1])# this will sort based on first element
print(sorted_data_2nd)

# sort based on the sum of each elements also reverse the order
sorted_data_sum_rev = sorted(data_2d, key=lambda x:x[0]+x[1], reverse=True)
print(sorted_data_sum_rev)

# map function transforms each element with a passed argument function
list1 = [1,2,3,4,5]
list2 = map(lambda x:x*2, list1)
print(list(list2))

#filter function takes a function which returns true or false and the filter function returns all the values for which the passed function evaluates true.
list3 = [0,1,2,3,4,5,6,7,8,9]
list4 = filter(lambda x:x%2==0,list3)# even numbers
print(list(list4))

# also with list comprehension
list5 = [x for x in list3 if x%2==0]# even numbers
print(list5)

# reduce take a function and a sequence and applys the function repetitively till it gives one value
from functools import reduce
a = [1,2,3,4,5,6]
prod_a = reduce(lambda x,y:x*y, a) # reduce function takes two arguments.
print(prod_a)