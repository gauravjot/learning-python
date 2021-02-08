from collections import deque

# lists are mutable, indexed, ordered and allow duplicate values

cars_list = ['BMW','Jeep','Honda']

# Iterating
print('The cars in list are:')
for car in cars_list:
    print(car)

print('The first car in list is', cars_list[0])

# lists can have different data types within

list = ["Alex", 22, True, 3.14]

print("The age of {} is {}".format(list[0], list[1]))

if (list[2]):
    print("The value of pi is", str(list[3]))

# list functions

cars_list.append('Toyota')

print("The number is items in car list is", len(cars_list))

print("Honda is {} on list".format(cars_list.index('Honda')))

print("Jeep is {} time/s in list".format(cars_list.count('Jeep')))

cars_list.reverse()

print("The reversed list:")
print(cars_list)

print("The list is sorted a-z:")
cars_list.sort()
print(cars_list)

# list as stack
# append() and pop() can be used to treat list like a stack
# where last-in first-out can be acheieved
# pop() returns the value which is deleted

print("Poping {} from cars list.".format(cars_list.pop()))

print(cars_list)

# list as queue, deque function is optimized for this feature
# popleft() can be used on a deque list
# to acheieve first-in first-out behaviour

print("Deque example:")
queue = deque(cars_list[:])
queue.popleft()
print(queue)

# del statement doesnt return a value on deletion
print("del example:")
del cars_list[0]
print(cars_list)

# Comprehension
print("\n")
even_numbers = [x*2 for x in range(1,10)]
print(even_numbers)

numbers_more_than_10 = [x for x in even_numbers if x > 10]
print(numbers_more_than_10)

# nested lists
nested_list = (('Apples', 'Banana', 'Mango'),('Pink','Red'),(3.14,9.80),False)
print(nested_list)