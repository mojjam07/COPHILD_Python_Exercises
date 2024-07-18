# Try it Yourself

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"{self.name} is the best in making {self.cuisine_type}.")
        
    def open_restaurant(self):
        print(f"{self.name} is now open.")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors:list):
        super().__init__(name, cuisine_type)
        self.flavors = flavors
        
    def display_flavors(self):
        for flavor in self.flavors:
            print(f"{flavor} flavour")
        
my_flavors = IceCreamStand('Sweet-Treats', 'Ice Cream', ['banana', 'mango', 'strawberry', 'orange'])
my_flavors.display_flavors()

       
restaurant = Restaurant('Boni-face', 'sardine-sauce')
restaurant1 = Restaurant('Eveling', 'pepper-sauce')
restaurant2 = Restaurant('Kings-guard', 'yummy-rice')
restaurant3 = Restaurant('Iya-Sunday', 'jollof-rice')

print(f"{restaurant.cuisine_type} is available at {restaurant.name} restaurant.")
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"{restaurant1.cuisine_type} is available at {restaurant1.name} restaurant.")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

print(f"{restaurant2.cuisine_type} is available at {restaurant2.name} restaurant.")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

print(f"{restaurant3.cuisine_type} is available at {restaurant3.name} restaurant.")
restaurant3.describe_restaurant()
restaurant3.open_restaurant()
