# Python has functions for creating, reading, updating, and deleting files.

# Open a file (open will create it, w mode is for writing it)
myFile = open('myFile.txt', 'w')

# Get some info on this file
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write("I love python")
myFile.write("... and Java")
myFile.close()

# Append to file after closing (a is for append)
myFile = open('myFile.txt', 'a')
myFile.write('\nI also like c++')
myFile.close()

# Read from file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)
