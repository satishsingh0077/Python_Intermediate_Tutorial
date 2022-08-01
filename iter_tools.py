# itertools are collections of modules to handle iterators.
#itertools: product, permutations, combinations, combinations_with_replacement, accumulate, groupby, and infinite iterators

# iterators are data types that can be used in a for loop

# Product: computes cartesian product of iterables
from audioop import mul
from itertools import groupby, product
from re import L
list1 = [1,2]
list2 = [3,4]
prod = product(list1,list2, repeat = 1) # gives the cartesian product of two lists. [(1, 3), (2, 3)]
print(list(prod))

#permutation : gives all possible orderings of an input
from itertools import permutations
list1 = [1,2,3]
perm = permutations(list1)
print(list(perm))
# we can also specify the length of the permutation
perm = permutations(list1, 2) # here we are specifying the length as 2
print(list(perm))

#combinations : gives all possible COmbinations of an input
from itertools import combinations
comb = combinations(list1,2)
print(list(comb))

#the above will not give the combinations with itself. to do that the module is called permutations_with _replacements

from itertools import combinations_with_replacement
comb_wr = combinations_with_replacement(list1,2)
print(list(comb_wr))

# accumalate : gives accumulated sum of an iterator. 
from itertools import accumulate
my_list = [1,7,2,4,5,6]
acc = accumulate(my_list)
print("mylist =  ", my_list)
print("accumulate =  ", list(acc))

# we can also pass an operator to accumulate function
import operator
acc = accumulate(my_list, func = operator.mul) # operator.max will give maximum
print("mylist =  ", my_list)
print("accumulate =  ", list(acc))

# groupby: helps in grouping iterables based on certian conditions. Returns keys and groups from an iterable
from itertools import groupby

my_list = [13,56,66,24,35,65,75,33,79,85]
# suppose we want to seperate the list into two parts baesed on a value ie >=40 and <40
def check_greater(x):
    if x >40 :
        return True
    else :
        return False

groupby_obj = groupby(my_list, key = check_greater)

for key,value in groupby_obj:
    print(key, list(value))

# we can also pass a lambda function as key.
groupby_obj = groupby(my_list, key = lambda x: x>50) #lambda takes input x and returns true if x>50
print(my_list)
for key,value in groupby_obj:
    print(key, list(value))
# more practical example
data = [{'name':'sat', 'age':25},{'name':'ish', 'age':26},{'name':'sin', 'age':27},{'name':'gh', 'age':28}] #array of dictionaries

# suppose we want to seperate then based on age
# using lambda as key to seperate based on condition that age is >26
seperated_data = groupby(data, key = lambda x: x['age']>26)
for key, value in seperated_data:
    print(key,  list(value))


# infinite iterators: iterations that can go to infinite
# count: counts from a point to infinity
from itertools import count
for i in count(1): #this will count from 1 to infinity unless u give a break
    print(i)
    if i>10:
        break

# cycle : cycles infinitely through an iterable
from itertools import cycle
cycle_list = [1,2,3]
#for item in cycle(cycle_list): #this will cycle infinitely unless inturrupted
#    print(item)

#repeat: repeats a certian number of time
from itertools import repeat
for i in repeat(cycle_list ,4): # this will repeat the input 4 times.
    print(i)