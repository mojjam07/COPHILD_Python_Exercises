'''
x = int(input("Enter first number: "))
op = input("Enter an operator: ")
y = float(input("Enter second number: "))


if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "*":
    print(x * y)
elif op == "/":
    print(x / y)
elif op == "//":
    print(x // y)
elif op == "**":
    print(x ** y)
elif op == "%":
    print(x % y)
else:
    print("Use a valid operator")
'''

x = 10
y = 20

#print(len(z))

if not(x <= y) and y >= x or x != y:
    print('Truth Statement')
else:
    print('False Statement')
    
# Using a single line expression, determine the output of the logical operator

e1 = 21
e2 = 15

if not(e1 <= e2) or e1 >= e2:
    print("Truth statement")
else:
    print("False statement")
    
