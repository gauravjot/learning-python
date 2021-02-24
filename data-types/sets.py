# sets do not allow duplicates and items cant be updated but can be added or removed
# sets are not sortable, unordered and unindexed thus a loop is required to iterate over items
# sets are defined with {} brackets

cars = {'honda','bmw','toyota','gmc'}
print(cars)

cars.add('audi')
print(cars)

cars.remove('honda')
print(cars)

# Popping last item from set, pop also returns popped item unlike remove()
cars.pop()
print(cars)

# Two sets can be merged: 'OR' operation
cars2 = {'mercedes','nissan','bmw'}
joined_cars = cars.union(cars2)
print(joined_cars)
# print(cars | cars2)

# we can get common items from two sets: 'AND' operation
print(cars & cars2)

# we can get items which are not common: 'XOR' operation
print(cars ^ cars2)

# we can remove a sets items from another set
print(cars - cars2)

# clearing set
cars.clear()
print(cars)