# product1 = {"name":"Scanner",
#             "quantity":45,
#             "price":4667.67
#             }

# qty = product1.get("name")
# print(qty)
# keyList = product1.keys()
# print(keyList)

# def checkProductAvailabilty(product: dict) -> bool:
#     if product.get("quantity") > 0:
#         return True
#     else:
#         return False

def performCalculation(number1, number2, operator) -> int:
    # try:
        if operator == "+":
            result =number1 + number2
            print(f"Addition of {number1} and {number2} = {result}")
        elif operator == "-":
            result = number1 - number2
            print(f"Subtraction of {number1} and {number2} = {result}")
            return result
        else:
            print(f"Invalid operator")
    # except Exception as error:
    #     print(error)
        

add = performCalculation(2,3,"+")
print(add)
# avaliable = checkProductAvailabilty(product1)
# print(f"Product availability status: {avaliable}")
