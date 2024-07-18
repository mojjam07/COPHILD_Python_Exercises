# Update Set
my_set1 = {1, 2, 3}
my_list = [4, 5, 6]

my_set1.update(my_list)
print(my_set1)

my_set1 != my_list # Shortcut
print(my_set1)

# Difference
set2 = {'apple', 'banana', 'cherry'}
set3 = {'google', 'microsoft', 'apple'}

x = set2.difference(set3)
y = set2 - set3 # Shortcut
print(x)
print(y)