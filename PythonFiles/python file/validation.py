u_name = input("Enter name: ")
password = input("Entet password: ")
c_password = input("Confirm password: ")

new_user = {'Username': u_name, 'Password': password}

users_db = []

if len(password) >= 6 and password == c_password:
    users_db.append(new_user)
    print("Registration Successful")
    
    for x in range(len(users_db)):
        if users_db[x]['Username'] == u_name and users_db[x]['Password'] == password:
            print("Welcome ", u_name, " to the system")
            print("Index number is ", x)
        else:
            print("Invalid users")
else:
    print("Password must exceed 6 character")