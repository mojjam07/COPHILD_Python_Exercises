users = list ({'user1':'teles', 'user2':'james', 'user3':'angel'})
newUser = input('Add user: ')
for key in users:
    if key == newUser:
        print(f'{newUser} already exist')
    else:
        users.insert(3, newUser)
        print(f'{newUser} added to users')
        print(users)
    break