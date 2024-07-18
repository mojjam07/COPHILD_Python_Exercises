# Function

y = 'Sodiq is coding'

def eat():
    global x
    
    x = 'Elliot is a guru'
    print(f'Inside - {x}')
    print(f'Inside - {y}')
    
eat()

print(f'Outside - {y}')
print(f'Outside - {x}')