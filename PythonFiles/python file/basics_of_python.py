var1 = "Hello, Python"
var2 = 23
var3 = 2.4
var4 = True

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

print('\n\n**** Operation of LIST in Python *****')

places = ["ikeja", "badagry", "idumota", "keju", "oshodi", "mushin", "agege", "apapa"]

print(f"\nThe list items are {places}")

# Accessing List elements with index

print(f"\nThe first element is {places[0].title()}")

# Changing, Adding & Removing elements from a list

# 1. Modifying a list
places[0] = "surulere"
print(f"\nAfter modifying the list, we have {places}")

# 2. Changing a list
places.append('iyana-ipaja')
print(f"\nAdding a place to the list : {places}")

# 3. Inserting element into a list
places.insert(1, 'isolo') #(pos, value)
print(f"\nAfter insert an element at index[1] : {places}")

# 4a. Removing element from a list with del
del places[1]
print(f"\nI just delete the element i just added : {places}")

# b. Removing elements using pop() function
popped_places = places.pop()
print(f"\nI used pop to pop-out the last element : {popped_places}")

popped_first = places.pop(0)
print(f"\nThis pop-out the element at its index : {popped_first}")

# c. Removing an item by its value
too_far = "badagry"
places.remove(too_far)
print(f"\nCheck the removed place in the list {places}")
print(f"\nThis {too_far} is too far..")

##### Organizing a list #####

# 1. Ordering a list with sorted() function

cars = ["toyota", "bmw", "audi", "volvo", "jeep"]

print(f"\nOriginal car list {cars}")

sorted_cars = sorted(cars) #...Why is this function not working?

print(f"\nThese are the sorted cars : {sorted_cars}")

# Printing list is reverse
#rev_cars = reversed(cars)
#print(f"\nThis is the reverse list : {rev_cars}")

print(f"\nI have {len(cars)} cars in my garage.")

##### Looping through list #####

print("\nWe are now working with loops\n")

schools =["ikhwan", "nasrullah", "KOK", "Al-qalam", "Qal'ah"]

for school in schools:
    print(f"In {school.title()}, you'll have a great knowledge.")
    print(f"Great students are from {school.capitalize()}.\n")

# doing something after loop
print("Thank you, and stay blessed.\n")


##### Making Numerical List #####

# Using range() function
for value in range(1, 6):
    print(value)


# Using range() to make a list of numbers
numb = list(range(1, 6))
print(f"\nThis is a list of numbers : {numb}.")

# Step size in range
numb = list(range(2, 11, 2))
print(f"\nThis is another list of numbers : {numb}.")

squares = []
for value in range(1, 11):
    #square = value ** 2
    squares.append(value ** 2)

print(f"\nSquare of 1-10 : {squares}.")

# Some simple statistics with numbers
digits = list(range(0,10))
print(f"\nThe minimum value is : {min(digits)}")
print(f"\nThe maximum value is : {max(digits)}")
print(f"\nThe sum of all the values is : {sum(digits)}")

##### List comprehension #####

squares = [value ** 2 for value in range(1, 11)]
print(f"\nThis is the result of list comprehension :\n{squares}")

##### Working with list part #####

## List Slicing

first_100 = list(range(5, 101, 5))

print(f"\nMy list : {first_100}")

print(f"\nFirst 5 : {first_100[0:5]}")

print(f"\nStart at 10 stop at 15 : {first_100[10:15]}")

print(f"\nLasst 5 : {first_100[15:]}")


##### Tuple Tuple Tuple #####

fruits = ("Orange", "Mango", "Banana", "Guava", "Pawpaw", "Cherry", "Pineapple")

# Indexing Tuples
print(f"\nThis is my tuple : {fruits}")
print(f"\nThis is the number 1 : {fruits[0]}")
print(f"\nThis is the last item : {fruits[-1]}")

# Looping through my tuple
print("\nThe tuple of my fruits")

for fruit in fruits:
    print(fruit)

#name = 'your name'
'''
while True:
    print('Please enter your name')
    name = input(':')
    if name != 'your name':
        continue
    print(f"Hello {name}, what is the password? it is {password}")
    password = input(':')
    if password == 'swordfish':
        break

print('Access granted, Thank you!')
'''