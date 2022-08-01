#string: ordered, immutbale, text representation

str1 = "Hello world"
print(str1)

#split the string
str1 = str1.split()
print(str1)

#join the string
str1 = " ".join(str1)# assign what has th be there in between. here we define space.
print(str1)

#formatting a string
# % method, same as c. %c=character, %d=integer, %s=string, %f=float
name = "satish"
age = 28
height = 6.0

final = 'My name is %s, my age is %d and my height is %.2f' % (name, age, height)
print(final)

#.format method
sentance = "Hello, my name is {}, I am {} years old and my height is {:.4f}".format(name,age,height)
print(sentance)

# fstring method
fsentance = f"hello world, I am {name}, {height:.3f} is my height and i am {age-1} years old"
print(fsentance)

# reverse the string
fsentance = fsentance[::-1] # nice trick to reverse a string.
print(fsentance)