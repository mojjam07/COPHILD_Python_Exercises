set1 = {4,7,7,5,4,6,5,7,5,3,21,0,6,8,9}
prices = set([4,7,7,5,4,6,5,7,5,3,21,0,6,8,9]) # Using Constructor
set2 = {2,5,4,6,9,5,7,5,3,21}
print(set1)
print(prices)
print(set2.intersection(set1))
print(set2.difference(set1))

for i in set1:
    print(i)