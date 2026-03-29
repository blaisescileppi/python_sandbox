# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'Brad'
age = 27

# concatenate
age = str(age)
print('hello, my name is ' + name + ' and I am ' + age)

# String Formatting

# arguments by position
print('my name is  {name} and i am {age}'.format(name=name, age=age))
# f strings
print(f'f string: hello my name is {name} and i am {age}')

# String Methods
s = 'hello world'
#capitalize string
print(s.capitalize())


# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('ld'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric false because space
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
