x = ['A', 'B', 'C', 'D','E','D','A','C']
a = ['A','B','C','D','E']
b = ['F', 'G', 'H', 'I','J']

x = ".".join(x)
print(x)

L = [1,2,3,4,5]
x = slice(2)
print(L[x])
'''
x.reverse()
x.remove('E')
print(x)
a.extend(b)
#print(a)

#c = a.append(b)
#print(a)
for i in b:
    c = a.append(i)
print(a)

y = {'A', 'B', 'C', 'D', 'E'}
z = {1, 2, 3, 4, 5}
w = {'name': 'mojjam'}

print(type(x)) # Ordered
print(x)
print(id(x[3]))
print(id(x[5]))
print(type(y)) # not ordered
print(y)
print(type(z)) # ordered cos it's numbers
print(z)
print(type(w))
print(w)
print(x.count('D'))
x.clear()
x.append('X')
print(x)


# 1. Length
print(f"I have {len(x)} elements in my list")

# 2. insert
x.insert(5, 'F')
print(f"I added a new letter to my list : {x}")

# 3. Delete
del x[:]
print(f"I have just deleted every items in my list : {x}")

# 4. Slicing

print(f"I purposely reduced my list items : {x[0:2]}")
'''