#List: ordered, mutable (HAS THE ABILITY TO BE CHANGED) and allows duplicate
# list is declared in []
list1 = ["Hello","World","canhaveduplicates",1,True,1.5]
print(list1)
#empty list
list2 = list()
print(list2)

#length of list
print(len(list1))

#iterate through list
for element in list1:
    print(element)

#index statrts with 0, list can have different data types
print(type(list1[4])) # will return boolena

# find element in list
print("Hello" in list1)

#append an item in list at end
list1.append("apple")
print(list1)

#insert at specific position
list1.insert(3,"banana") #index and element as argument
print(list1)

# clear the list
list1.clear()
print(list1)

#remoeve element from end
list1 = ["apple","banana","cherry",1,True, "lion"]
list1.pop() #returns tha last element and removes it
print(list1)

#remove a cretian element
list1.remove(True) #understand the catch here, 1 is treated as ture so it will delete 1.
# also remove menthod will remove only the first occurance of the match and above proves the same
# 0 and 1 are treated as true and false
print(list1)

#sort the list in ascending order
#list1.sort() # will only work if datatypes of elemnt in list are same
#print(list1)

#to get new sorted list, use list1 = sorted(list1)

#create list with same value
list2 = [0]*5
print(list2)

# slicing the list
list3 = [0,1,2,3,4,5,6,7,8,9]
print(list3[0:5])# this will exclude the last index
# specifying step
print(list3[0:5:2]) # this will take every second index
# reverse the list and a trick
list3.reverse()
print(list3)
list3 = list3[::-1]# this will reverse the list
print(list3)

#copying a list
#if we assign a new list to original list then both the links refer to the same list
#and modifying one will effect the other, thus below is used
list3_copy = list3.copy()
print(list3_copy)

#list comprehension
list3_square = [x*x for x in list3]
print(list3_square)

#count the number of repetitions of an element in a list
list1 = [1,2,3,4,1,23,3,4,5,1,2,4,5,6]
print(list1.count(1))#3 times
print(list1.count(True))# will also return 3 as 1 = true

list2 = [True,False,True,True,True,False,False]
print(list2.count(True))# 4
print(list2.count(1))# 4 as true  = 1
print(list2.count(0)) # 3 as 0 = False

#index of an element
print(list2.index(True))#returns the index of first occurance

#unpacking
list3 = "satish",28,"Magdeburg"
name,age,city = list3 #number of elements on left must match the number of elements in the tuple
print(name)
print(age)
print(city)