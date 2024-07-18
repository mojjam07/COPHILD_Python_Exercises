# Class and object => class is a template for creating other objects
# Class is a blueprint for creating objects
# object is an instance of a class

# 4 pillars of OOP

class RegisteredUser:
    
    #constructor
    def __init__(self, user_email, user_password) -> None:
        self.email = user_email
        self.password = user_password

    def changePin(self, oldPassword, newPassword) -> bool:
        if oldPassword == self.password:
            self.password = newPassword
            return True
        return False

    def getPin(self):
        return self.password


class BankUser(RegisteredUser):
    
    def __init__(self, email, starting_balance,pin = "1234") -> None:
        super().__init__(user_email=email , user_password=pin)
        self.balance = starting_balance



    def transfer (self, receiver, amount, pin):
        if self.balance < amount:
            print(f'Amount is too low... Topup {amount-self.balance} more')
            return False

        if self.getPin() != pin:
            print(f'Incorrect Pin')
            return False

        if not isinstance(receiver, BankUser):
            print(f'Reciever is not a registered user')
            return False

        self.balance -= amount
        receiver.balance += amount
        print('Successfull')
        return True
        
        

    


user1 = BankUser('atejiri@outlook.com', 20000, 't6w7w7whwhwhs3')
user2 = BankUser('helen23@outlook.com', 1000, 'jdjd783j3')

#user1.transfer(user2, 1000,'t6w7w7whwhwhs3')
user1.transfer(user2, 1000,'t6w7w7whwhwhs3')