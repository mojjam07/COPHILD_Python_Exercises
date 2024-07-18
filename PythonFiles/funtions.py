

# def greetUser(name : str) ->  None :
#     print(f'Hi {name.upper()}, Welcome!')
# greetUser('Jae5')
# greetUser('Airlee')

# def addNumber(numb1 : int or float, numb2 : int or float) -> float or int :
#     return numb1 + numb2
# result = addNumber(4,6.7)
# print(result)

myList = [
    {'item':'Milk', 'price_per_unit': 350, 'quantity': 2},
    {'item':'Egg', 'price_per_unit': 100, 'quantity': 6},
    {'item':'Tissue', 'price_per_unit': 400, 'quantity': 3},
    {'item':'Bread', 'price_per_unit': 400, 'quantity': 2},
    {'item':'McVites', 'price_per_unit': 730, 'quantity': 4}
]

def calculate_total_price(myList : int) -> int :
    total_price = 0

    for item in myList:
        price_per_unit = item.get('price_per_unit')
        quantity = item.get('quantity')
        total_price += price_per_unit * quantity

    return total_price

total_price = calculate_total_price(myList)
print(f'Total Price: #{total_price}')