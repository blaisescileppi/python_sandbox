# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 5
z = 40


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple If
if x > y:
    print(f'{x} is greater than {y}')

# If/else
if x > z:
    print(f'{x} is greater than {z}')
else:
    print(f'wrong. {x} < {z}')

z = 10
# elif
if x > z:
    print(f'{x} is greater than {z}')
elif x == z:
    print(f'{x} = {z}')
else:
    print(f'wrong. {x} < {z}')

# Nested if
if x > 2:
    if  x <= 10:
        print(f'{x} is greater that 2 and less than or equal to 10')

if x > 2 and x <= 10:
    print(f'{x} is greater that 2 and less than or equal to 10')

# or
if x > 2 or x <= 10:
    print(f'{x} is >2 or <= 10')

# not
if not(x==y):
    print(f'{x} != {y}')

# Logical operators (and, or, not) - Used to combine conditional statements ^^




# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
numbers = [1, 2, 3, 4, 5]
a = 2
b = 6
if a in numbers:
    print(a in numbers)

if b not in numbers:
    print(b not in numbers)

c = b
if b is c:
    print(b is c)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
