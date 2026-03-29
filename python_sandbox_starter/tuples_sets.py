# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# print(fruits)

# single value tuple needs a trailing comma to be a tuple, otherwise it's a string
fruits2 = ('Apples')
fruits3 = ('Apples',)
# print(fruits2, type(fruits2), fruits3, type(fruits3))

# get value
print(fruits[1])

# CANT change tuple value
# fruits[0] = 'Pear' # TypeError: 'tuple' object does not support item assignment

# Delete tuple
del fruits2
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.
# Create a set
fruits_set = {'Apples', 'Oranges', 'Mango'}
# Check if in set
print('Apples' in fruits_set)

fruits_set.add('Grape')
print(fruits_set)

# remove value
fruits_set.remove('Grape')
print(fruits_set)

# clear a set
fruits_set.clear()
print(fruits_set)

del fruits_set
print(fruits_set)
