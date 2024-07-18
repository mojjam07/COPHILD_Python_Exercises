class Employee:
    
    # class variable
    num_of_employee = 0
    pay_rise = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        self.num_of_employee += 1
        
    # method of class
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
    def apply_raise(self):
        self.pay = int(self.pay * self.pay_rise)

# instance of a class    
emp_1 = Employee('Jamiu', 'Mojeed', 2500)
emp_2 = Employee('Jamiu', 'Mubarak',
 2510)

print(emp_1.email)
print(emp_2.email)

emp_1.apply_raise()
emp_2.apply_raise()

print(emp_1.pay_rise)

print(emp_1.pay)
print(emp_2.pay)

print(emp_1.num_of_employee)
print(emp_1.num_of_employee)

print(emp_1.fullname())
print(emp_2.fullname())

'''
--- Note ---
1. caps in class naming
a. constructor method
2. self conventional parameter
3. instance(s) of class
4. method(s) of class and its calling with parenthesis
'''