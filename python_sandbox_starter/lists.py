# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
numbers = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'grapes', 'pears']

# Use a constructor
numbers2 = list((1, 2, 3, 4, 5))

# print(numbers, numbers2)

# get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('mangos')

print(fruits)

# Remove values
fruits.remove('grapes')
print(fruits)

# Insert into position
fruits.insert(2, 'strawberries')
print(fruits)

# remove with pop, reverse
fruits.pop(2)
fruits.reverse()

print(fruits)
#sort (alphabeticxally)
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)


#change value
fruits[0] = 'blueberries'
print(fruits)
