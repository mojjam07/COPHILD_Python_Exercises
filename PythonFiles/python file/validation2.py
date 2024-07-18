user_name = input("\nEnter your username: ")
password = input("\nEnter a password: ")
conf_password = input("\nConfirm your password: ")

new_user = {'user_name' : user_name, 'password' : password} # username and password caged here

users_db = []

# This if statement is responsible for validation of inputs
if len(password) >= 6 and password == conf_password:
    users_db.append(new_user)
    print("\nRegistration Successful")
    
    # This for loop is responsible for checking if username and password
    for x in range(len(users_db)):
        if users_db[x]['user_name'] == user_name and users_db[x]['password'] == password:
            print("\nWelcome", user_name ,"to your portal")
            print("\nYou're currently at index", x)
        else:
            print("Invalid user!")
            
else:
    print("\nPasswword must be more than 6 letters")