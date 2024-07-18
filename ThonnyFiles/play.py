'''
name = "    Abdul Mojeed   "

print(name)
print(name.strip().upper().replace(' ', ''))
print(name.rstrip())
print(name.lstrip())


numb = 14_000_000_000

print(numb)

guests = ["jeniffer", "marvellous", "ibrahim", "sarah", "adepeju"]

abs_guests = guests.pop(3)

print(abs_guests)

print(guests)

print(f"Hello {guests[0].capitalize()} you're invited to my dinner.")
print(f"Hello {guests[1].capitalize()} you're invited to my dinner.")
print(f"Hello {guests[2].capitalize()} you're invited to my dinner.")
print(f"Hello {guests[3].capitalize()} you're invited to my dinner.")
#print(f"Hello {guests[-1].capitalize()} you're invited to my dinner.")

#new_guests = guests.insert(3, "kemi")

print(f"\n{abs_guests.capitalize()} will not be coming again.")
print(f"{guests[3]} will replace {abs_guests.title()} that is not available.")
'''

places = ["Saudi Arabia", "Kuwait", "London", "America", "Barcelona"]

print(f"My Original list:{places}\n")

places.reverse()
print(f"My Reversed list:{places}\n")

sorted_places = sorted(places)
print(f"My Sorted list:{sorted_places}\n")

print(f"My Original list:{places}")