my_dictionary = {'house':'where we live', 'toilet':'rest room', 'kitchen':'where we cook', 'iron':'laundry tool', 'bucket':'for bathing'}

# Accessing dictionary
print(my_dictionary['kitchen'])

# Length of dictionary
print(len(my_dictionary))

# Adding to dictionary item
my_dictionary['bed'] = 'where we sleep'

print(my_dictionary)

# New length of my_dictionary
print(len(my_dictionary))

# Accessing item in  my_dictionary
print(my_dictionary['bed'])

# Removing item from my_dictionary
del my_dictionary['kitchen']

print(my_dictionary)

# Using get() to access values
a_val = my_dictionary.get('dinning', 'where we eat as a family')
print(a_val)
# This work as an exception, if we're accessing a value that's not present in the dictionary.

##### Try it yourself Exercise #####

info = {'fname': 'musharraf', 'lname': 'jamiu', 'age': 15, 'city': 'ikeja'}

print(f"\nFirst Name : {info['fname'].title()}")
print(f"\nLast Name : {info['lname'].title()}")
print(f"\nAge : {info['age']}")
print(f"\nCity : {info['city'].title()}")

##### 2 #####
fav_numb = {'jemeelat': 10, 'mojeed': 7, 'mubarak': 20, 'aduke': 9, 'musharraf': 2 }

print(f"\nJemeelat was born on April {fav_numb['jemeelat']}th")
print(f"\nMojeed was born on September {fav_numb['mojeed']}th")
print(f"\nMubarak was born on December {fav_numb['mubarak']}th")
print(f"\nMubarakat was born on May {fav_numb['aduke']}th")
print(f"\nMusharraf was born on December {fav_numb['musharraf']}nd")

fav_numb['malik'] = 21
fav_numb['eniola'] = 8
fav_numb['mardiyyah'] = 19

print(f"\nAbdul Malik was born on January {fav_numb['malik']}st")
print(f"\nEniola was born on June {fav_numb['eniola']}th")
print(f"\nMardiyyah was born on April {fav_numb['mardiyyah']}th")


##### 3 #####
p_terms = {'key': 'keys', 'value': 'values', 'pair': 'pairs', 'access': 'accessing', 'print': 'prints'}

print(f"\n{p_terms['key']} is the one holding the values")

print(f"\n{p_terms['value']} is the one held by the keys")

print(f"\n{p_terms['pair']} is the name given to keys the values")

print(f"\n{p_terms['access']} is the way of getting the values in a dictionary")

print(f"\n{p_terms['print']} is done through {p_terms['access']} ")


##### Looping through dictionaries ####

for key, value in p_terms.items():
    print(key,':',value)
    

### looping through all the keys or values ###

for key in p_terms.keys():
    print(key)
    
    
for value in p_terms.values():
    print(value)
    


##### Sieving practice #####
    
favourite_languages = {'python': 'mojjam', 'javascript': 'taiwo', 'java': 'isibor', 'c++': 'aliu', 'c#': 'ujunwa'}

languages = []
friends = []

for friend, language in favourite_languages.items():
    friends.append(friend.title())
    languages.append(language.title())
print(friends)
print(languages)

##### Looping through dictionary in an order #####

for lang in sorted(favourite_languages.keys()):
    print(lang.upper())
    
for friend in sorted(favourite_languages.values()):
    print(friend.upper())
    
print("\n\n##### Try it yourself! #####")

python_terms = {"print": "gives output", "variable": "storage location", "if/elif/else": "conditonal statement"}

for key,value in python_terms.items():
    print(key, ':', value)


print()
python_terms["for/while"] = "for looping through items"
python_terms["dictionary"] = "store key/value pairs"
python_terms["list"] = "store list items"


for key,value in python_terms.items():
    print(key, ':', value)
    

print("2.\n")

rivers = {"nile": "egypt", "niger": "nigeria", "han": "korea"}

for name, country in rivers.items():
    print(name.title(), "runs through", country.title())
    
print("\nWe have the following rivers:")

for name in rivers.keys():
    print(name.title())

print("\nThe rivers are found in:")
for country in rivers.values():
    print(country.title())
    
    
print("\n3.\n")

poll_list = ["isibor", "kanu", "taiwo", "dupe", "mojjam"]

for poll in poll_list:
    if poll in favourite_languages.values():
        print(f"Thank you {poll.title()} for participating")
    else:
        print(f"Ensure you participate {poll.title()}")
        
##### List of dictionaries #####      
print(f"\nList of Dictionaries\n")

house_1 = {'color':'white', 'address': 12, 'height' : 'tall'}
house_2 = {'color': 'blue', 'address': 21, 'height' : 'short'}
house_3 = {'color':'red', 'address': 9, 'height' : 'medium'}

street = [house_1, house_2, house_3]

print(street)


print(f"\nList of 30 houses in an estate")

estate = []

for street in range(1, 31):
    new_house = {'color':'red', 'address': 9, 'height' : 'medium'}
    estate.append(new_house)

print(len(estate), 'houses completed.')

# display the first 5 houses #
for houses  in estate[:5]:
    print(f"\nHouse number : {houses}")
    
    
#### A list in dictionary ####

store = {'box A': ['money', 'cloth', 'shoes'], 'box B': 'kitchen utensils' }

print()

for s in store['box A']:
    print(s)
    

#### A dictionary in dictionary ####

shop = {'beverages': {'coke': '20 piece', 'fanta': '15 pieces', 'pepsi': '10 pieces' }, 'morsels': {'amala': '5 wraps', 'fufu': '6 wraps', 'semo': '10 wraps'}}

print()

for m in shop['morsels']:
    print(f'{m}')
    
    
##### Try it yourself #####
print("\n##### Try it yourself #####\n")

info_1 = {'fname': 'musharraf', 'lname': 'jamiu', 'age': 15, 'city': 'ikeja'}

info_2 = {'fname': 'malik', 'lname': 'moshood', 'age': 8, 'city': 'kola'}

info_3 = {'fname': 'mubarak', 'lname': 'alabi', 'age': 8, 'city': 'bariga'}

people = [info_1, info_2, info_3]

for person in people:
    print(person)
print('......')

pet_1 = {'type': 'cat', 'age': 3, 'owner': 'alabi'}
pet_2 = {'type': 'fish', 'age': 4, 'owner': 'malik'}
pet_3 = {'type': 'dog', 'age': 6, 'owner': 'ben'}
pet_4 = {'type': 'chicken', 'age': 7, 'owner': 'eniola'}
pet_5 = {'type': 'rabbit', 'age': 2, 'owner': 'beebah'}

pets = [pet_1, pet_2, pet_3, pet_4, pet_5]

for pet in pets:
    print(f"\nThe {pet['type'].title()} is {pet['age']} weeks old, it belongs to {pet['owner'].title()}")
    
f_places = {'nigeria': {'abuja': 'gwagwalada', 'lagos': 'oshodi', 'ibadan': 'mapo'}, 'spain' : {'catalonia': 'barcelona', 'andalus': 'sevilla'}}

#users = input("Enter a country name: ")
#place = input("Enter your favourite place: ")

#### Chat GPT ####

# Define the dictionary
favorite_places = {
    "Alice": ["Paris", "Kyoto", "New York"],
    "Bob": ["Beach", "Mountains"],
    "Charlie": ["Venice", "Sydney"]
}

# Loop through the dictionary and print favorite places for each person
for person, places in favorite_places.items():
    print(f"\n{person}'s favorite places are: {', '.join(places)}")
