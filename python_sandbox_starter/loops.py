# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
people = ['john', 'paul', 'sarah', 'susan']

# for person in people:
#     print(f'current person: {person}')

for a in people:
    print(f'first example current person: {a}')

# Breaking out of a loop
for person in people:
    if person == 'sarah':
        break
    print(f'second example current person is: {person}')

# Continue (skip)
for person in people:
    if person == 'sarah':
        continue
    print(f'third example current person is: {person}')
 
# Range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f'number: {i}')

# While loops execute a set of statements as long as a condition is true.
count = 0 
while count <= 10:
    print(count)
    count += 1