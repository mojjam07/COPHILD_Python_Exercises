# List practice solutions

my_guests = ["kemi", "kudi", "kaka", "kofi"]

print(f"hi {my_guests[0]}, you're invited to my dinner")
print(f"hi {my_guests[1]}`, you're invited to my dinner")
print(f"hi {my_guests[2]}, you're invited to my dinner")
print(f"hi {my_guests[3]}, you're invited to my dinner")

abs_guest = my_guests.pop(1)
print(f"\nOops! {abs_guest} won't be coming")

my_guests.insert(1, 'kope')
print(f"\n{my_guests[1]} will replace {abs_guest} at the dinner")

print(f"\nMy new guest list : {my_guests}")

print(f"\nhi {my_guests[0]}, you're invited to my dinner")
print(f"hi {my_guests[1]}`, you're invited to my dinner")
print(f"hi {my_guests[2]}, you're invited to my dinner")
print(f"hi {my_guests[3]}, you're invited to my dinner")

my_guests.insert(2, 'kira')
my_guests.insert(4, 'kure')
my_guests.append('kuro')

print(f"\nI now have more guests : {my_guests}")

print(f"\nhi {my_guests[0]}, you're invited to my dinner")
print(f"hi {my_guests[1]}, you're invited to my dinner")
print(f"hi {my_guests[2]}`, you're invited to my dinner")
print(f"hi {my_guests[3]}, you're invited to my dinner")
print(f"hi {my_guests[4]}, you're invited to my dinner")
print(f"hi {my_guests[5]}, you're invited to my dinner")
print(f"hi {my_guests[6]}, you're invited to my dinner")

print(f"\nOnly two (2) can attend my dinner.")

print(my_guests)

rem_1 = my_guests.pop(0)

print(f"\nSorry, {rem_1} has be removed")
rem_2 = my_guests.pop(1)
print(f"Sorry, {rem_2} has be removed")
rem_3 = my_guests.pop(2)
print(f"Sorry, {rem_3} has be removed")
rem_4 = my_guests.pop(3)
print(f"Sorry, {rem_4} has be removed")
#rem_5 = my_guests.pop(-6)
#print(f"Sorry, {rem_5} has be removed")

print(f"\nMy invited guests : {my_guests}")

print(f"\nDespite everthing, {my_guests[0]}, you're still invited.")
print(f"Despite everthing, {my_guests[1]}, you're still invited.")
print(f"Despite everthing, {my_guests[2]}, you're still invited.")

del my_guests[0]
del my_guests[1]
del my_guests[-1]

print(f"\nAt the end, I have {my_guests} list")

print("\n\n These are five (5) places i'll like to visit in the world.")

places = ["mecca", "kuwait", "barcelona", "london", "jordan"]

print(f"\nHere are the places : {places}")

places_ord = sorted(places)
print(f"\nCheck the order : {places_ord}.")

#places.sort(reverse = True)
print(f"\nThe original list : {places}.")

rev_ord = reversed(places) #peoblem here
print(f"\n{rev_ord}") #peoblem here

print(f"\nOriginal order : {places}.")

# Another practical
'''
for val in range(1, 21):
    print(val, end=',')
    
numb = list(range(1, 1000001))
print(numb)

print(f"\nThe min is :{min(numb)}")
print(f"\nThe max is :{max(numb)}")
print(f"\nThe sum is :{sum(numb)}")
'''

print("These are odd numbers:")  

odds =[]
for val in range(1, 21):
    if val % 2 != 0:
        print(val, end=',')

print("\n\nThese are multiples of 3 numbers:")        

for val in range(3, 31):
    if val % 3 == 0:
        print(val, end=',')
        
print("\n\nWorking with SLICE in list")

list_items = list(range(1, 11))

print(f"\nThe first three of my list are :{list_items[:3]}")
print(f"\nThe three items from the middle of my list are :{list_items[4:7]}")
print(f"\nThe last three of my list are :{list_items[-3:]}")


