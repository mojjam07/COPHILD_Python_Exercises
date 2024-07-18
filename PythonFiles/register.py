def register_user():
    print('Welcome to the registration page')

    username = input('Enter your username: ')
    password = input('Enter your password: ')
    email = input('Enter your email: ')

    current_registration = {
        'Username': username,
        'Password': password,
        'Email': email
    }
    
    registrations = []
    registrations.append(current_registration)
    print('\nRegistration successful! Details')
    print(f'Username: {username}')
    print(f'Password: {password}')
    print(f'Email: {email}')

    
    print('\nAll Registration:')
    for index, x in enumerate(registrations, start=1):
        print(f'{index}. {x}')

    login = input('Enter your username: ')
    passkey = input('Enter your password: ')
    
    for user in range(len(registrations)):
        if login == registrations[user]["Username"] and passkey == registrations[user]["Password"]:
            print(f'{username} login successfully!')
        else:
            print(f'{username} not found')

register_user()