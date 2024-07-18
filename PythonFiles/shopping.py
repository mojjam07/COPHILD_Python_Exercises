myCart = [
    {'item': 'bag', 'unit_price': 200, 'quantity': 4},
    {'item': 'shoe', 'unit_price': 530.6, 'quantity': 3},
    {'item': 'cap', 'unit_price': 150.76, 'quantity': 7},
    {'item': 'jean', 'unit_price': 1100, 'quantity': 1},
    {'item': 'top', 'unit_price': 500, 'quantity': 5},
]

def addTotalPriceToDict(myCarts):
    for item in myCarts:
        item['total_price'] = item['unit_price'] * item['quantity']
    return myCarts

addTotalPriceToDict(myCart)
print(myCart)
# def calculate_total_price() -> int or float:
#     totalPrice = 0
#     for item in myCart:
#         unit_price = item.get('unit_price')
#         quantity = item.get('quantity')
#         totalPrice += unit_price * quantity
#     return totalPrice

# totalPrice = calculate_total_price()
# print(f'Total Price: #{totalPrice}')