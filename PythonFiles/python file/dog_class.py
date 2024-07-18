# A simple class (Dog) definition
class Dog:
    # Class attribute for all instances
    #species = "Canis familiaris"
    
    # Constructor to initialize instance attr.
    def __init__(self, name, breed):
        self.name = name # Attribute 1
        self.breed = breed # Attribute 2
        
    # A method for the class (Dog)    
    def bark(self):
        return f"{self.name} barks"
        
my_dog = Dog("Fido", "Canis familiaris")

print(my_dog.name)
print(my_dog.bark())