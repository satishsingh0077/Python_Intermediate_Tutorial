# sets: unordered, mutable but doesnot allow duplicates
# defined inside {}
set1 = {1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1,0} #duplicate values will be removed
print(set1)
set1 =set("Hello World") #only unique values will stay
print(type(set1))
print(set1)
print(len(set1))#here we get the value as 8 because 8 unique characters are there in Hello world(including space)
#NOTE:- This is a nice and easy way to find out number of unique characters in word.

#add and remove element
set1.add('k')
print(set1)
set1.remove('H')
print(set1)

#union and intersection
oddset = {1,3,5,7,9}
evenset = {0,2,4,6,8}
primeset = {1,2,3,5,7}

#union combines the sets
union_odd_even = oddset.union(evenset)
print(union_odd_even)
#union returns a new set, it nevwe updates the original set.
#to update the set, use setA.update(setB). This will make setA that has all the values of satA nad SetB

#intersection keeps what is common between the two
intersection_odd_prime = oddset.intersection(primeset)
print(intersection_odd_prime)
#intersectionupdate method will can be used to modify a set

#difference gives all elements from one set that are not in second
diff_odd_prime= oddset.difference(primeset)
print(diff_odd_prime)#9

diff_prime_odd= primeset.difference(oddset)
print(diff_prime_odd)#2

#setA.isdisjoint(setB) can be used to see if there is no common elelemnts among them

#symentic difference = se1+set2 -(common in set1 and set2)
sym_diff_prime_odd = primeset.symmetric_difference(oddset)
print(sym_diff_prime_odd)#2,9

#subset and superset
setA= {1,2,3,4,5,6,7,8,9,0}
setB = {7,8,9}
print(setA.issubset(setB))#false
print(setB.issubset(setA))#true

print(setA.issuperset(setB))#true
print(setB.issuperset(setA))#false

#a forozen set is an immutable set
f_set = frozenset([1,2,3,4])
print(type(f_set))
#adding and removing is not permitted