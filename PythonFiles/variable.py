# Names = 'Elliot'
# print(id(Names))
# Name = 'Elliot'
# print(id(Name))
# x = Name.isupper()
# print(type(Name))
# y = len(Name)
# print(type(y))



# Age = 23
# x = Age.is_integer()
# print(x)

# Person = 'All'
# y = Person.rfind('l')
# print(y)
# z = id(Person)
# print(z)

# num = 23.6764452534
# y = int(num)
# print(y)

Name = input('Enter Your Name: ')
Year = input ('Enter Year of Birth: ')
current = 2024
Age = current- int(Year)

if Age <= 18:
    print(Name," You're not eligible to apply")
else:
    print(Name," You're", Age, "Years Old")

x = ['mojjam', 'banna', 'mojjam']
for i in x:
    if i == x[0]:
        print(i, 'is a duplicate')
        break
    else:
        print(i, 'is not a duplicate')

