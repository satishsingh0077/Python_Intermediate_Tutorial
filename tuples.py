# tuple: ordered, immutable (can not be changed) and allows duplicate elements
#tuple is delcared in ()
tuple1 = ("apple","orange","banana","apricot")
print(tuple1)

#tuple can also be declared like below
tuple1 = "hello","world" # or tuple1 = tuple(("cat","dog","mouse"))
print(tuple1)
print(type(tuple1)) #class tuple

#if only one element is declared in tuple, python treats it as a string
tuple1 = ("apple")
print(type(tuple1)) # class string
# to overcome this a "," must be added at the end
tuple1 = ("apple",)
print(type(tuple1)) # class tuple

# tuples can be indexed just like list but with the use of [], not ()
print(tuple1[0]) # apple

#gety count of elenents
print(tuple1.count("apple"))
print(tuple1.count("a"))

#unpacking a tuple
tuple3 = "satish",28,"Magdeburg"
name,age,city = tuple3 #number of elements on left must match the number of elements in the tuple
print(name)
print(age)
print(city)

#unpacking multiple elements with wild card
tuple4 = 1,2,3,4,5,6,7
i1,*i2,i3 = tuple4
print(i1) #return first lements
print(i2)# returns all the elements in between in a form of list
print(i3) #returns the last element

#tuples are more memory and time effecient compared with list