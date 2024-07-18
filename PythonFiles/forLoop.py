print("Get Registered Today")
userName = input("Enter Username..... ").lower()
password = input("Enter Password..... ").lower()
confirmPass = input("Confirm Password..... ").lower()
newUser = {"userName":userName, "password": password}
users_db = []

if len(password) >= 4 and password == confirmPass:
        users_db.append(newUser)
        print(userName,"registration successful!")
        for x in range(len(users_db)):
                if users_db[x]["userName"] == userName and users_db[x]["password"] == password:
                        print("Welcome",userName,"to the system")
                        print("The index number of the registered user is", x)
                        break
                else:
                        print("Invalid User")
else:
        print("Password must exceed 6char, start over!")
                        