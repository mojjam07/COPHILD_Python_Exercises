class Cat:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def naming(self):
        return "My Cat name is " + self.name
    
    def sounding(self):
        return self.name + " gives sound " + self.sound
        
        
my_cat = Cat('Nani', 'meow')
print(my_cat.naming())
print(my_cat.sounding())