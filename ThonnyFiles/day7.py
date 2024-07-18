product1 = {"name":"scanner", "quantity": 50, "price": 465.7}

qty = product1.get("quantity")
print(qty)
val = product1.values()
print(list(val))
key = product1.keys()
print(list(key))

for key in product1:
    print(f"Key is {key} and value is {product1.get(key)}")

# pylance

# functions