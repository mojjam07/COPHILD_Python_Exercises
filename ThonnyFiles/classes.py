# Creating and Using a class

class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        print(f"{self.name} rolled over.")

# Making an instance(attribute) from a class
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

# Accessing Attributes
print(f"My dog name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old")
print(f"Your dog name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old")

# Calling methods
my_dog.sit()
my_dog.roll_over()
your_dog.sit()
your_dog.roll_over()