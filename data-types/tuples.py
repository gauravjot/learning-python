# tuple items are ordered and unchangeable. It does allow duplicates
# tuple is restrictive list as item cant be altered, rmeoved or added freely
# tuple is defined with () instead of [] in case of list

mytuple = ('Banana','Mango','Apple','Coconut','Peach')
print(mytuple)
print(type(mytuple))

print("The last item in tuple is",mytuple[-1])

print("The items before index 3", mytuple[:3])

print("The items after index 2",mytuple[2:])

print("The items from index 1 upto 3", mytuple[1:3])

print("The index of Apple is",mytuple.index('Apple'))

print("Mango is this many times in tuple", mytuple.count('Mango'))

# If ever need to update a tuple, only way is to convert to list

print("\nUpdating tuple:")
mylist = list(mytuple)
mylist.append('Orange')
mytuple = tuple(mylist)
print(mytuple)

# * astericks notation

print("\nAstericks usage:")
(fruit_frist,*fruit_others,fruit_last) = mytuple
print(fruit_frist)
print(fruit_others)
print(fruit_last)

# without bracket

print("\nWithout bracket:")
new_tuple = 'hello','world',True,22
print(new_tuple)