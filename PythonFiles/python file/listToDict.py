price_list = ['$5', '$10', '$15', '$20', '$25']

def convertToDict(prices):
    db = {}
    count = 1
    
    for price in prices:
        price = float(price.replace('$', ''))
        db[f'price{count}'] = price
        count += 1
    return db
    
def sumList(prices):
    total = 0
    
    for price in prices:
        price = float(price.replace('$', ''))
        total += price
    return total
        
print(convertToDict(price_list))
print(sumList(price_list))