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
'''
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
'''
# Correction

priceList = ['$5', '$20', '$12', '$14', '$10']

def convertAndSum(prices):
    total = 0 # Create a variable to store the sum
    for price in prices:
        price = price.replace('$', '') # Remove the $ symbol
        price = float(price)	# Convert it to float
        total += price # Sum 
    return total

print(convertAndSum(priceList))

# 3.
'''
def price(prices : list):
    db = {}
    for p in range(0, len(prices)):
        db[prices[p]] = prices[p]
    return prices

#price_db = {title: prices[p]}
prices = [5, 20, 12, 14, 10]
print(price(prices))
'''
priceList = ['$5', '$20', '$12', '$14', '$10']

def convertListToDictionary(prices):
    count = 1 # Create a variable to store the sum
    price_dict = {} # Create an empty dictionary
    
    for price in prices:
        price = float(price.replace('$', '')) # Remove the $ symbol and convert to float
        
        price_dict[f"Price{count}"] = price
        
        count += 1 # Increment the count to change it value
    return price_dict

print(convertListToDictionary(priceList))