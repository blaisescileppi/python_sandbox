# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create a dict
person = {
    'first_name': 'john',
    'last_name':  'doe',
    'age': 37,
}
print(person, type(person))
# use a constructor
# person2 = dict(first_name = "Sarah", last_name = "Williams")

# Get value

print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'
print(person2)

# Remove item
del(person['age'])
person.pop('phone')
print(person)

#clear person
person.clear()
print(person)

# get length
print(len(person2))

# List of dictionaries
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Billy', 'age': 25},
    {'name': 'Andy', 'age': 41},
]

print(people)
print(people[1]['name'])