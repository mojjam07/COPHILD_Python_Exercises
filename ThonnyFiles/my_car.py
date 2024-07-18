# Importing multiple classes from a module
from class_car import Car, ElectricCar

# Importing entire module
import class_car

# Import All classes from a module
from class_car import *

# Using Aliases
from class_car import ElectricCar as EC

#from class_car import Car
#from class_car import ElectricCar

my_new_car1 = Car('audi', 'a4', 2019)
my_new_car2 = Car('volvo', 'v5', 2022)

my_new_electric_car1 = Car('tesla', 'T500', 2022)

print(my_new_car1.descriptive_name())
print(my_new_car2.descriptive_name())

print(my_new_electric_car1.descriptive_name())