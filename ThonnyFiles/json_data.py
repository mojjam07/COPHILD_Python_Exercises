# list => Array
# str => sting
# int or float => integer
# dict => object
# bool => boolean
# None => null

# Application Programming Interface (API)

import json

prices = "true"
print(type(prices))

prices = json.loads(prices)
print(type(prices))

ages = [56, 45]
print(type(ages))

ages = json.dumps(ages)
print(type(ages))