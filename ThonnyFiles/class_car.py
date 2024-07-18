# Working with Classes and Instances

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
my_car = Car('audi', 'a4', 2019)
print(my_car.descriptive_name())


# Setting default value for an attribute

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # default value set here
        
    def descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        print(f"The car has {self.odometer_reading} miles on it")
    
my_car = Car('audi', 'a4', 2019)
print(my_car.descriptive_name())
my_car.read_odometer()


# Modifying Attribute values

# :: Directly through an instance

my_car.odometer_reading = 20
my_car.read_odometer()


# INHERITANCE

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # default value set here
        
    def descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        print(f"The car has {self.odometer_reading} miles on it")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        
        

my_tesla = ElectricCar('tesla', 'TS32', 2023)
print(my_tesla.descriptive_name())

# Defining Attributes and Methods for child class

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # default value set here
        
    def descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        print(f"The car has {self.odometer_reading} miles on it")
    
    def fill_gas_tank(self):
        print("What will happen here!")
        
class Battery:
    # A simple instance to model an electric car battery
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")
        
    #def update_battery(self):
        
    
class ElectricCar(Car): # Inheritance here
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        #self.battery_size = 75
        self.battery_size = Battery()
        
    def describe(self):
        print(f"The car has a {self.battery_size}-kWh battery.")
        
    def fill_gas_tank(self): # Override will happen here
        print("Electric car doesn't need gas tank")
        
        

my_tesla = ElectricCar('tesla', 'TS32', 2023)
my_tesla_battery = Battery()
#print(my_tesla.descriptive_name())
#my_tesla.describe()
my_tesla.fill_gas_tank()
my_tesla_battery.describe_battery()