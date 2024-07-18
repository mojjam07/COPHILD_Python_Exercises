class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'
        
    def fullname(self):
        return "{} {} got {} pay monthly.".format(self.fname, self.lname, self.pay)

emp_1 = Employee("Jamiu", "Mojeed", 20000)
emp_2 = Employee("Jamiu", "Mubarak", 10000)

print(emp_1.email)
print(emp_1.fullname())
print(emp_2.fullname())