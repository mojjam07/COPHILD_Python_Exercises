'''
count = 1

while count <= 5:
    print(count)
    count += 1
    

# Asking users for input

prompt = "\nEnter a message"
prompt += "\nType 'quit' to quit the program: "

msg = ''
while msg != 'quit':
    msg = input(prompt)
    print(msg)
print("Thank you!")


# Using a flag

prompt = "Enter a message"
prompt += " Or type 'quit' to quit\n:"

active = True

while active:
    msg = input(prompt)
    
    if msg == 'quit':
        active = False
    else:
        print(msg)
        

# Using 'break' to exit a while loop

prompt = "Type the name of the cities"
prompt += " Or type 'quit' to quit\n:"


while True:
    msg = input(prompt)
    
    if msg == 'quit':
        break # here it comes
    else:
        print(f"I've visited {msg.title()}")


# Using 'continue' in a while loop

c_numb = 0

while c_numb < 10:
    c_numb += 1
    if c_numb % 2 == 0:
        continue
    
    print(c_numb)
    


# Avoiding infinite loop

x = 1

while x <= 5:
    x += 1 # Take note of this to avoid i.l
    print(x)
    


# Try it yourself #

#1

msg = "Write the type of pizza you like"
msg += " Or type 'quit' to exit the program\n:"

open = True

while open:
    prompt = input(msg)
    
    if prompt == 'quit':
        open = False
    else:
        print(prompt)
        
#2

age = 0

while True:
    age = int(input('\nHow old are you: '))
    
    if age <= 3:
        print("You're free to watch with 0$")
    elif age >= 3 and age <= 12:
        print("You're to pay $10 for a ticket")
    else:
        print("You're to pay $15 for a ticket")



# Using a while loop with list and dictionary

unconfirmed = ['mark', 'janet', 'abeni', 'suliat', 'joseph']
confirmed = []

while unconfirmed:
    current = unconfirmed.pop()
    
    print(f"Verifying user : {current.title()}")
    confirmed.append(current)

print("\nThe following has been confirmed: ")
for confirm in confirmed:
    print(confirm.title())
    

# Removing all instances of specific values from a list

pets = ['cat', 'dog', 'fish', 'rat', 'rabbit', 'dog', 'calf']

print(pets)

while 'dog' in pets:
    pets.remove('dog')
    
print(pets)


# Filling a dictionary with user input

## polling app

responses = {}

#set a flag
polling = True

while polling:
    #prompt for u.name and response
    name = input("\nWhat is your name: ")
    response = input("\nWhich mountain do you like: ")
    
    #store the response in dict
    responses[name] = response
    
    #find out if anyone else is taking part
    repeat = input("Would you like to participate (yes/no) : ")
    if repeat == 'no':
        polling = False
        
#polling is complete. show result
print("\n--- Poll Result ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")



## Try it yourself ##
# 1
sandwish_orders = ['pastrami','pepperish','pastrami', 'sharwama', 'salad', 'pastrami', 'porridge']

finished_sandwish = []

while sandwish_orders:
    order = sandwish_orders.pop()
    
    print(f"\nI made you {order.title()} sandwish")
    finished_sandwish.append(order)
    
for sandwish in finished_sandwish:
    print(f"\n{sandwish.title()}")

print("The deli has ran out of pastrami")

while 'pastrami' in finished_sandwish:
    finished_sandwish.remove('pastrami')
    
print("These are the available sandwish:", finished_sandwish)
'''
# 2

location = {}
vacation = True

while vacation:
    name = input('Your name: ')
    query = input('Where do you wanna visit: ')
    
    location[name] = query
    
    repeat = input('You want another quiz? (yes/no): ')
    if repeat == 'no':
        vacation = False

print('--- Thank You ---')
for name, query in location.items():
    print(f"{name} wants to visit {query}")
