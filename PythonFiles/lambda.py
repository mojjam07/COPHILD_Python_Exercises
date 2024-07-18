# add = lambda x,y,z,f: print(x + y + z + f)
# add(5,3,2,4)


# def subtract(a,b):
#     return(a - b)
# c = subtract
# print(c(4,3))

# def extendSubtract(func:subtract, a,b,c):
#     result = func(a,b)
#     return(c * result)

# print(extendSubtract(subtract,5,2,2))


# myCart = [
#     {'item': 'bag', 'unit_price': 200, 'quantity': 4},
#     {'item': 'shoe', 'unit_price': 530.6, 'quantity': 3},
#     {'item': 'cap', 'unit_price': 150.76, 'quantity': 7},
#     {'item': 'jean', 'unit_price': 1100, 'quantity': 1},
#     {'item': 'top', 'unit_price': 500, 'quantity': 5},
# ]
# def addTotalPriceToDict(item: dict):
#     items = item.copy()
#     items['total_price'] = items['unit_price'] * item['quantity']
#     return items
# mapped_result = map(addTotalPriceToDict, myCart) 

# print(list(mapped_result))
# print(myCart)

# myCart = [
#     {'item': 'bag', 'unit_price': 200, 'quantity': 4},
#     {'item': 'shoe', 'unit_price': 530.6, 'quantity': 3},
#     {'item': 'cap', 'unit_price': 150.76, 'quantity': 7},
#     {'item': 'jean', 'unit_price': 1100, 'quantity': 1},
#     {'item': 'top', 'unit_price': 500, 'quantity': 5},
# ]

# myCart = [
#     {'item': 'bag', 'price': 100, },
#     {'item': 'shoe', 'price': 530.6 },
#     {'item': 'cap', 'price': 150.76 },
#     {'item': 'jean', 'price': 1100 },
#     {'item': 'shirt', 'price': 50},
# ]

# def discountPrice(discount: dict):
#     item = discount.copy()
#     item['discount'] = (10/100)* item['price'] 
#     return item



# mapped_result = map(discountPrice, myCart)

# # print(list(mapped_result))
# # print(myCart)

# def filterLessThan15(item):
#     return item['discount'] >= 15

# def filterWrap(product: list):
#     mapped_product = map(discountPrice,product)
#     filtered = filter(filterLessThan15, mapped_product)
#     return list(filtered)

# print(filterWrap(myCart))

            
myClass = [
    {'name':'Alvin', 'score':87},
    {'name':'Helen', 'score':55},
    {'name':'Pamela', 'score':38},
    {'name':'Collins', 'score':92},
    {'name':'Philip', 'score':71},
    {'name':'Miraj', 'score':40},
    {'name':'James', 'score':65}
]

def assign_grade(class_record: list) -> list:
  
  add_key = lambda class_record: {**class_record, 'grade': grade(class_record['score'])}
  return list(map(add_key, myClass))


def grade(score):

    if score >= 100:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    elif score >= 50:
        return 'E'
    else:
        return 'F'
    
    
classGrades = assign_grade(myClass)
for n in classGrades:
    print(f'{n['name']} - Score: {n['score']}, Grade: {n['grade']}')

print('----------------')

from functools import reduce

def combine_records(record1, record2):
    return {'score': record1['score'] + record2['score']}

def calculate_average_grade(class_record: list) -> list:
    total_score = reduce(combine_records, myClass)['score']
    average_score = total_score / len(myClass)
    average_grade = grade(average_score)
    return average_grade

# Assuming the 'assign_grade' and 'grade' functions are already defined

average_grade = calculate_average_grade(myClass)

print(f"Class Average Grade: {average_grade}")





    
























