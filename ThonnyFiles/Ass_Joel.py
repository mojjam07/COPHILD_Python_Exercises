### Assignment ###

# 1. 

def my_function(fruits : list):
    for fruit in fruits:
        if fruits == []:
            print('You have an empty list')
        else:
            firstItem = fruits[0]
            lastItem = fruits[-1]
    return firstItem, lastItem

my_fruits = ['mango', 'banana', 'pawpaw', 'orange']
my_function(my_fruits)
result = my_function(my_fruits)
print(f"The first item is {result[0]} and the last item is {result[-1]}")

# 2.
from operator import *

priceList = ['$5', '$20', '$12', '$14', '$10']
realPriceList = []
total = 0

for price in priceList:
    actualPrice = float(price.replace('$', ''))
    realPriceList.append(actualPrice)
for realPrice in realPriceList:
    total = add(realPrice, total)
print(f"The total price is ${total}")

# 3.
def price(prices : list):
    for p in prices:
        return p

price_db = {title: prices[p]}
prices = [5, 20, 12, 14, 10]
print(prices)
