NAME = "Mojjam"
print(id(NAME))

NICKNAME = "Mojjam"
print(id(NICKNAME))

########## Keywords ###########
# lambda
# True
# False
# and
# or
# in
# if
# elif
# else
# as
# class
# is
# def
# del
# while
# for
# except
# break
# await
# global
# try
# import
# raise
# None
# from
# pass
# not
# assert
# not

Name = "Congratulations"

x = Name.isupper()
print(type(Name))

Name2 = "Mojjam"
Name2 = len(Name2)
print(Name2)

### Class work: Using primary data types, create a program that outputs other data types ###

### string ==> boolean
Name3 = '350'
Name3 = Name3.isdigit()
print(Name3)

### float ==> integer
Name4 = 34.6
Name4 = round(Name4)
print(Name4)

### string ==> integer
Name5 = "Mathematics"
Name5 = Name5.index("i")
print(Name5)

### Type Casting
x = '243'
y = int(x)
print(y)

x = 4.8231
y = int(x)
print(y)

x = 4
y = float(x)
print(y)

#### Registration form ###########

#name = input('Enter your name: ')
#year = int(input('Enter your year of birth: '))
#current_year = 2024
#age = current_year - year

#if age <= 18:
    #print(name, "You're not eligible to apply")
#else:
    #print(name, "You're ", age, "year old")


x = ['Mojjam', 'Banana', 'Mojjam']

for i in x:
    if i == x[1]:
        print(i, 'is a duplicate')
        #break
    else:
        print(i, 'is not a duplicate')