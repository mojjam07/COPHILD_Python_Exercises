# Mr. Joel - function

# 1.

def checkQtyAvailability( product : dict ) -> bool :
    if product.get('quantity') > 0:
        return True
    else:
        return False
    
item = {
    'name' : 'Printer',
    'quantity' : 20  
}
is_available = checkQtyAvailability(item)
print(f"Product availability : {is_available}")

# 2.

def performCalculation(num1, num2, op):
    if op == '+':
        result = num1 + num2
        print(f"Additon of {num1} and {num2} = {result}")
    elif op == '-':
        result = num1 - num2
        print(f"Subtraction of {num1} and {num2} = {result}")
    elif op == '*':
        result = num1 * num2
        print(f"Multiplication of {num1} and {num2} = {result}")
    else:
        print('Operator defined not found')

performCalculation(32, 40, '+')
performCalculation(32, 50, '-')
performCalculation(32, 32, '*')
performCalculation(32, 10, '/')