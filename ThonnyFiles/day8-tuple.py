# Array -> List
# Object -> Dictionary

# Data Structure
    # Linear
        # Static
            # Array
        # Dynamic
            # Queue
            # Stack
            # Linked list
    
    # Dynamic
        # Tree
        # Graph
        
# Tuple
x = ('A', 'B', 'c')
#print(x.pop())
#print(x.insert(0, 'D'))
#print(x.append('D'))
x = list(x)
x[0] = 'Z'
x[-1] = 'Z'
y = x[1:4]
print(y)
x = tuple(x)
print(x)
print(type(x))

# Removing item from a list

my_list = ['A', 'B', 'C', 'D', 'E']
my_turple = ('E', 'B', 'D', 'C', 'A')
my_t = list(my_turple)
my_t.remove(my_t[0])
print(my_t)

# Unpacking variables
x = ('prof', 'ujunwa', 'eliot', 'marv')
(man, lady, boy, human) = x
print(man)
(x, *y, z) = x
x = (x, *y, z)
print(y)
print(z)
#print(x, *y, z)

my_dict = {'E':'e', 'B':'b', 'D':'d', 'C':'c', 'A':'a'}
my_set = {'E', 'B', 'D', 'C', 'A'}

one_item = ('F',)
print(my_turple + one_item)

add_tuple = ('F', 'G')
add_tuple = list(add_tuple)



y = my_list[1:4]
p = my_list[-4:-1]

my_list.extend(add_tuple)
conv = tuple(my_list)
print(conv)

print(y)
print(p)

print(f"List : {len(my_list)}")
print(f"Tuple : {len(my_turple)}")
print(f"Dictionary : {len(my_dict)}")
print(f"Set : {len(my_set)}")

zen = ('prof', 'ujunwa', 'eliot', 'marv')
z = list(zen)
den = ('bola', 'tola')
d = list(den)
z.extend(d)
print(z)

#for i in zen:
#    print(i.title())
    
newName = input('Enter name: ')

name = ['ujunwa', 'professor', 'eliot', 'mojjam']
#name[1] = newName
#print(name)

if type(name) == list:
    name[1] = newName
    print(name)
elif type(name) == tuple:
    print('Not changeable')
else:
    print('None of the above')