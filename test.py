# input = abcaba
# output = abcaabbaaa

inp = input("Enter a string:  ")
mydict = {}
mystr = ""
for elem in inp:
    if elem in mydict:
        mydict[elem] = mydict[elem] + 1
        mystr = mystr + (elem*mydict[elem])
    else:
         mydict[elem] = 1
         mystr = mystr + elem

print(mydict)
print(mystr)
