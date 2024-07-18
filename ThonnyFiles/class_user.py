# 2.
class Priviledges:
    def __init__(self, priviledges):
        self.priviledges = priviledges

    def show_priviledges(self):
        for priviledge in self.priviledges:
            print(f"Admin {priviledge}")

class User:
    def __init__(self, firstName, lastName, age, gender, address):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.gender = gender
        self.address = address
    
    def describe_user(self):
        print(f"I am {self.lastName} {self.firstName}, {self.age}years old, from {self.address} state.")
        
    def greet_user(self):
        print(f"A {self.gender} named {self.firstName} is greeting you!")


class Admin(User):
    def __init__(self, firstName, lastName, age, gender, address, priviledges:list):
        super().__init__(firstName, lastName, age, gender, address)
        #self.priviledges = priviledges
        self.priviledges = Priviledges(priviledges)
        
    
priv = ['can add post', 'can delete post', 'can ban user']
adminPriv = Admin('Mojeed', 'Jamiu', 29, 'male', 'osun', priv)
adminPriv.priviledges.show_priviledges()


user1 = User('Mojeed', 'Jamiu', 29, 'male', 'osun')
user2 = User('Dunmola', 'Taiwo', 26, 'female', 'ondo')
user3 = User('Hassanah', 'Yahya', 30, 'female', 'kano')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()