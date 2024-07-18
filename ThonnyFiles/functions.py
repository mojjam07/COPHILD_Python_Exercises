'''
# Defining a function

def greet_user():
    # simple message 
    print('Hello')
    
greet_user()


# passing information to a function

def greet_user(username):
    print('hello', username.title())
    
greet_user('mojjam')


# Try it yourself #

#1.

def display_message():
    print('A message to a console')
    
display_message()

# 2.

def favourite_book(title):
    print(f"My favourite book is {title.title()}")
    
favourite_book('game of thrones')

# Passing arguments

def pet_description(petType, petName):
    print(f"My pet is {petType} and it's called {petName}.")
    
pet_description('cat', 'nani')
pet_description('dog', 'pent')

# Keyword arguments

def pet_description(petType, petName):
    print(f"My pet is {petType} and it's called {petName}.")
    
pet_description(petName='paddy', petType='rabbit') # default value
pet_description(petName='dog', petType='pent')

# Default value

def pet_description(petName, petType='goat'):
    print(f"My pet is {petType} and it's called {petName}.")
    
pet_description('cat', 'nani')
pet_description('dog')


# Try it yourself #

def make_shirt(size, message):
    
    print(f"My barca jersey is size {size}, and has {message} printed on it.")
    
make_shirt(23, 'Messi')
make_shirt(message='Ronaldinho', size=30)

def describe_city(name, country):
    print(f"{name.title()} is in {country.title()}.")
    
describe_city('jamiu', 'germany')
describe_city(country='canada', name='aduke')
describe_city('benjamin', 'berlin')

# Returning values

def format_name(firstName, lastName):
    # print out a well formatted name
    fullName = f"my name is {firstName.title()} {lastName.title()}"
    return fullName
    
details = format_name('mojeed', 'jamiu')
print(details)

# Making argument optional

def format_name(firstName, lastName, middleName=' '):
    if middleName:
        fullName = f"{lastName} {firstName} {middleName}"
    else:
        f"{lastName} {firstName}"
        
    return fullName.title()
    
details1 = format_name('mojeed', 'jamiu', 'adekunle')
details2 = format_name('mubarak', 'jamiu')
print(details1)
print(details2)

# Returning a dictionary

def human(firstName, lastName):
    # Returning a dict of info
    person = {'first_name': firstName , 'last_name': lastName}
    
    return person
    
detail = human('mojeed', 'jamiu')
#print(type(detail))
print(detail)

# Using a function in a while loop

def format_name(fistName, lastName):
    fullName = f"{fistName} {lastName}"
    return fullName.title()

while True:
    print("\nPlease Enter your name")
    print("(enter 'q' to quit the program)") # To control the loop
    f_name = input('First Name: ')
    if f_name == 'q': # To control the loop
        break
    l_name = input('Last Name: ')
    if l_name == 'q': # To control the loop
        break
    obj = format_name(f_name, l_name)
    print(f"Hello {obj}!")


# Try it Yourself
#1
def city_country(name, country):
    city = f"'{name}, {country}'"
    return city.title()

city1 = city_country('santiago', 'chile')
city2 = city_country('gwagwalada', 'nigeria')
city3 = city_country('medinah', 'saudi-arabia')

print(city1)
print(city2)
print(city3)

#2
def make_album(artist, album):
    album = {'artist': artist, 'album': album}
    return album
    
album1 = make_album('nice', 'gongo-aso')
print(album1)
album2 = make_album('akon', 'gangstar')
print(album2)
album3 = make_album('asake', 'challenge')
print(album3)

#3
def make_album(artist, album):
    album = {'artist': artist, 'album': album}
    return album

while True:
    print("\nAnswer the question\nOr type 'q' to quit.")
    artiste = input('Input artist name: ')
    if artiste == 'q':
        break
    albume = input('Input album name: ')
    if albume == 'q':
        break
    
    obj = make_album(artiste, albume)
    print(obj)
    

# Passing a list

def greet_user(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)
        
user = ['mojjam', 'mubby', 'aduke']
greet_user(user)

# Modifying a list in a function

unprocessed = ['rubber', 'cotton', 'wood', 'seed']
finished = []

print("\n") # just for spacing

while unprocessed:
    current = unprocessed.pop()
    print(current)
    
    finished.append(current)
    
print('The following has been printed:')
for finish in finished:
    print(finish)


# Using function to modify a list in a function

def models(unprocessed, finished):
    
    while unprocessed:
        current = unprocessed.pop()
        print(current)
        
        finished.append(current)
        
def show_models(finished):
    print("The following are finished")
    for finish in finished:
        print(finish)
        
unprocessed = ['rubber', 'cotton', 'wood', 'seed']
finished = []

models(unprocessed, finished)
show_models(finished)

# Try it Yourself

def short_text_msgs(messages):
    for message in messages:
        print(f"{message}")

#def send_msg(sent_msg):
    

obj = ['Hey bro', 'How far', 'Whatsup', 'Wetin dey', 'how you']
short_text_msgs(obj)


def send_msg(sent_msg: list):
    for msg in sent_msg:
        print(msg, end='')
        sent_msg.append(msg)


sent_msg = []
for sent in sent_msg:
    print(sent)
obj = ['Hey bro', 'How far', 'Whatsup', 'Wetin dey', 'how you']
#send_msg(obj)
send_msg(sent_msg)


# Passing Arbitrary Number of Arguments

def shoping(*my_cart):
    print(my_cart)
    
#buyerA = input(':')
shoping('bread')

#buyerB = input(':')
shoping('buscuit', 'chin-chin', 'garri', 'candies')


# Mixing Positional and Arbitrary arguments

def breakfast(plates, *foods):
    print(f"I ate {plates}-plates of the of the following foods:")
    for food in foods:
        print(food)
    
breakfast(2, 'semo', 'amala')
breakfast(4, 'rice', 'beans', 'asaro', 'gbegiri')

# Storing Your functions in Modules

# :: Importing an entire module
import food # from a file named food.py in the same directory

food.make_food(2, 'Amala', 'Semovita')
food.make_food(4, 'Rice', 'Beans', 'Yam', 'Fruits')


# :: Importing Specific
from food import make_food

make_food(2, 'Amala', 'Semovita')
make_food(4, 'Rice', 'Beans', 'Yam', 'Fruits')


# :: Using as to give function an alias
from food import make_food as mk

mk(2, 'Amala', 'Semovita')
mk(4, 'Rice', 'Beans', 'Yam', 'Fruits')


# :: Using as to give Module an alias
import food as f

f.make_food(2, 'Amala', 'Semovita')
f.make_food(4, 'Rice', 'Beans', 'Yam', 'Fruits')


# :: Importing all function in a Module
from food import *

make_food(2, 'Amala', 'Semovita')
make_food(4, 'Rice', 'Beans', 'Yam', 'Fruits')
'''
