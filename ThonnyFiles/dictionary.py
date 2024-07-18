my_dictionary = {'color':'green', 'point': 5}

# Accessing dictionaries
print(my_dictionary['color'])
print(my_dictionary['point'])

# Adding values to a dictinary
my_dictionary['amount'] = 20
my_dictionary['price'] = 15

#print(my_dictionary)

# Modifying values in dictionary
my_dictionary['color'] = 'yellow'
print(f"My dictinary is now color '{my_dictionary['color']}'")

#print(my_dictionary)

alien = {'x_pos': 0, 'y_pos': 25, 'speed': 'medium'}

print(f"Orignal position: {alien['x_pos']}")

#move the alien to the right
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
    
alien['x_pos'] = alien['x_pos'] + x_increment

print(f"New position: {alien['x_pos']}")