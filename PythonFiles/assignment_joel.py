# def detectEmptyList (myList: list):
#     if myList ==[]:
#         print("The list is empty")
#     else:
#         print(f'The first item:, {myList[0]}')
#         print(f'The last item:, {myList[0-1]}')

# user_hobbies = []
# reveal = detectEmptyList(user_hobbies)
# print(reveal)

    

priceList = [ "$5", "$20", "$12", "$14", "$10"]
'''
prices = [float(price[1:]) for price in priceList]
total = sum(priceList)
'''

def convertAndSum(prices : list):    
    # create a variable to store the sum
    total = 0

    # create a loop
    for price in prices:
        # remove the $ symbol
        price : str = price.replace("$","")

        # now convert the string to a float
        price = float(price)

        # now sum it to the total
        total += price

    return total

def convertToDictionary(prices : list):    
    # create a variable
    count = 1
    price_dict = {}

    # create a loop
    for price in prices:
        # remove the $ symbol and convert to float
        price : float = float(price.replace("$",""))

        price_dict[f'price{count}'] = price

        # now increase count to change it value
        count += 1
        

    return price_dict

print(convertAndSum(priceList))
print(convertToDictionary(priceList))