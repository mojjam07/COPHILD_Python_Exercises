#Parameter = Variable
#Argument = Value

def name(a,b,c,d):
    pass

name('a','b','c','d')

# Arbitrary keyword Argument
def mummy(**kids):
    print(type(kids))

mummy() 

def mummi(*kids):
    print(type(kids))

mummi('john','dammy','akin')

def mumma(name = 'Emeka'):
    print('My name is', name)
    
mumma()
mumma('Mojjam')
mumma('Seun')


def mylist(param : list):
    print(param[3])
    
mylist(['kola','seun','ose','uju'])

def mylist(param):
    print(param[0])
    
items = ['messi','ronaldo','halland']
mylist(items)

name = ['uju','elliot','prof']
def my_name(name):
    print('my name is', name)
    
my_name(name[1])

# Return function

def function():
    x = 2
    y = 4
    z = x * y
    

    if z >= 2:
        print(2)
    else:
        print('wrong')
    return z

function()
#print(function())

