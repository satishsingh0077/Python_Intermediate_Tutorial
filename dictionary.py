#dictionary: key-value pair, unordered, mutable
#declared withn {} and each key, value pair seperated by :
dict1 = {1:"apple",2:"orange",3:"banana"}
print(dict1)

#dictonary can also be declared as 
dict2 = dict(name = "John", age = 36, country = "Norway")
print(dict2)

#invalid identifier
#dict3 = dict(1="apple",2="orange",3="banana")
# the above will result in error because 1,2,3 are not valid identifiers and dict expects valid identiifers
# Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore _. 
# Names like myClass, var_1 and print_this_to_screen, all are valid example.
# An identifier cannot start with a digit. 1variable is invalid, but variable1 is a valid name.
# Keywords cannot be used as identifiers.

#accessing items
print(dict1[1])
print(dict2["name"])# in this case we have to surround the key with quotes because in dict method, the key is a string

#adding entries to dictionary
dict2["pin"]=384848
print(dict2)

#id same key is used to assign aggain, the value will be updated
dict2["pin"]=123456
print(dict2)

#deleting
del dict2["name"]
print(dict2)
# another method
dict2.pop("age")
print(dict2)
#anothermethod
dict2.popitem() #this will remove the last item
print(dict2)

dict2 = dict(name = "John", age = 36, country = "Norway")
#check in dictionary
if "country" in dict2:
    print(dict2["country"])
else:
    print("not found")
# using for loop
for key,value in dict2.items():
    print(key, value)

#update the dictionary
dict1 = dict(name = "John", age = 36, country = "Norway", email = "abc@gmail.com")
dict2 = dict(name = "sam", age = 34, country = "England", pin = 6678877)

dict1.update(dict2) # the common fiels will ubdate and unique fiels from both will retain
print(dict1)

#using tuple as key
tuple1="apple","mango"
dict4 = {tuple1:"fruits"} # here tuple is assigned as key
print(dict4)
# note that a list can not be assigned as a key because it is mutable
for key in dict4.keys():
    print(key)

print(dict4[("apple","mango")]) # example of using tuple as key. This will return fruits