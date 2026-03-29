# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create a class
class User:
    # Constructor: a function that runs when u instantiate an object or a class
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return(f'My name is {self.name} and I am {self.age}')
    
    def hasBirthday(self):
        self.age += 1



# init user object
blaise = User('blaise', 'test@test.com', 25) 

print(blaise.age)
blaise.hasBirthday()
print(blaise.greeting())

# Extend a class
class Costumer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def setBalance(self, balance):
        self.balance = balance

    def greeting(self):
        return(f'My name is {self.name} and I am {self.age} and my balance is {self.balance}')


janet = Costumer('janet', 'janet@email.com', 65)
janet.setBalance(500)
print(janet.greeting())

    