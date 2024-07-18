# scope 

p = 45


def findX():
    global x 
    x = 45
    print(x)

    def findY():
        y = 30
        print(x)
        print(y)
    findY()
   
p = [20,22]

def manipulate(d):
    d.append(99)

findX()
print(x)

manipulate(p)

print(p)