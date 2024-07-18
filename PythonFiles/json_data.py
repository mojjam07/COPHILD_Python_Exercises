
# list => array
# str => string
# int or float => number
# dict => object
# bool => boolean
# None => null 
import json 

prices = "true"
print(type(prices))

prices = json.loads(prices)
print(type(prices))

ages = [56,45]
print(type(ages))
ages = json.dumps(ages)
print(type(ages))