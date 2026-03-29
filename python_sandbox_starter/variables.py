# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

''' multiline comment '''
# single line comments

x = 1 # int
y = 2.5 # float
name = "john" #string
is_cool = True # bool must be uppercase

# multiple assignment
x, y, name, isCool = (1, 2.5, 'john', True)

#Output
print('Hello')
print(x)
print(x, y, name)

#basic math
a = x + y
print(type(x))

# casting
y = int(y)
print(type(y), y)