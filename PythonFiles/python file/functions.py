# Defining a function

def greet_user():
    ''' simple message '''
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
    ''' print out a well formatted name '''
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
    '''Returning a dict of info'''
    person = {'first_name': firstName , 'last_name': lastName}
    
    return person
    
detail = human('mojeed', 'jamiu')
#print(type(detail))
print(detail)