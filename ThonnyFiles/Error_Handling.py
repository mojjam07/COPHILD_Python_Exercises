# hackerank / turing / starcode / andelar

def performCalculation(num1, num2, op):
    try:
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
    except Exception as error:
        print(error)

performCalculation(32, 40, '+')
performCalculation(32, 50, '-')
performCalculation(32, 32, '*')
performCalculation(True, None, '*')
performCalculation(32, 10, '/')

### Assignment ###

def my_function(fruits : list):
    return fruits.pop(0), fruits.pop()

my_fruits = ['mango', 'banana', 'pawpaw', 'orange']
result = my_function(my_fruits)
print(f"The first item on my fruit list is {fruits.pop(0)}\nWhile the last item there is {fruits.pop()}")