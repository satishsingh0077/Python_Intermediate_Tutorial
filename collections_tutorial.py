# collection :Counter, namedtuple, orderedDict, defaultdict, deque
# Counter :  it is a container that stores element as dictionary keys and their count as dictionary values

#****************************************************************************************************************************
# notes: When you use a dependency, eg. in this case it is collections and Counters, make sure the name of the python script 
# is not same as the depencency else it will throw ImportError
#****************************************************************************************************************************

from collections import Counter
var = "Hello World"
my_counter = Counter(var)
print(my_counter)
print(my_counter.most_common(1))# will return list of tuples, the most common [(l,3)]
print(my_counter.most_common(2))# will return list of tuple with 2 most common [(l:3),(0,2)]
print(list(my_counter.elements()))# will return all the elements the same unmber of times they occur ['H', 'e', 'l', 'l', 'l', 'o', 'o', ' ', 'W', 'r', 'd']


# namedTuple : easy to create light weight object type, similar to structure
from collections import namedtuple
student = namedtuple('student', 'name,age') # this is same as declaring a class student with fields name and age
s1 = student("satish", 28) # similar to creating object
print(s1.name, s1.age)

# ordered dictionary: remebmers the order in which the data is entered. 
# Irrelivent after python 3.7 because the basic dictionary will also rember the order.

# defaultdict: it is similar to the normal dictionary with the only exception that it will have a default value if the key is not set yet.
from collections import defaultdict
int_default_dict =defaultdict(int) # here we are creating a default dict which will return the dafault value of integer, when you try to retrieve a key value wwhich does not exists
int_default_dict['a']="apple"
int_default_dict['b']="ball"
int_default_dict['c']="cat"

print(int_default_dict) #defaultdict(<class 'int'>, {'a': 'apple', 'b': 'ball', 'c': 'cat'})
print(int_default_dict['c']) #returns cat
print(int_default_dict['d']) # will return default value of int i.e. 0 since the value key pair for d is not set
# a normal dictionary will raise an KeyError exception in the above case.

# deque: this is a double ended queue. can be used to add/ remove elements from both sides.
from collections import deque
de_list = deque()
de_list.append(1)
de_list.append(2)
print(type(de_list)) #<class 'collections.deque'>
print(de_list)
# append to the left
de_list.appendleft(0)
de_list.appendleft(-1)
print(de_list)
# extend 
de_list.extend([3,4,5])
print(de_list)
de_list.extendleft([-2,-3,-4]) # -4 will be the leftmost element
print(de_list)
#rotate
de_list.rotate(2)# all elements will rotate "right" by 2 spots
print(de_list)
de_list.rotate(-2)# all elements will rotate "left" by 2 spots
print(de_list)