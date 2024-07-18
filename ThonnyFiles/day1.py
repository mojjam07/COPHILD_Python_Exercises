name1 = "Dammy"
name1 = name1.lower()

print(name1)

name2 = "mummy"
name2 = name2.capitalize()
print(name2)

name3 = "Elephant"
name3 = name3.upper()
print(name3)

name4 = "Encourage"
name4 = name4.find('u')
print(name4)

name5 = "Laundry"
name5 = name5.replace('dry', 'ch')
print(name5)

name6 = "Money"
name6 = name6.isalpha()
print(name6)

name7 = "Money"
name7 = name7.isdigit()
print(name7)

name8 = "Money"
name8 = name8.isspace()
print(name8)

name9 = "MONEY"
name9 = name9.isupper()
print(name9)

name10 = "MONEY"
name10 = name10.startswith('K')
print(name10)

print("Next 10 string method")

name11 = "Most of you guys are trying"
name11 = name11.title()
print(name11)

name12 = "Most of you guys are trying"
name12 = name12.strip()
print(name12)

name13 = ("Let", "love", "lead")
name13 = " ".join(name13)
print(name13)

name14 = "Most of you guys are trying"
name14 = name14.endswith('s')
print(name14)

name15 = "Most of you guys are trying"
name15 = name15.index('g')
print(name15)

name16 = "Most of you guys are trying"
name16 = name16.casefold()
print(name16)

name17 = "Most of you guys are trying"
name17 = name17.count('y')
print(name17)

msg = "Most of you guys are trying"

for i in msg:
    print(i.count('y'))

print("Let's make it dynamic")

dyn = "Ujunwa"

if dyn.islower():
    print("All characters are lower case")
else:
    print("No, look into your code properly")
    
    
info = "Attention Needed"
info = info.startswith('N')
print(info)

info = "Attention Needed"
info = info.startswith('N', 10, 15)
print(info)