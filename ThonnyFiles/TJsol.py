msg="Attention Needed"

x=[]
y=[]

for i in msg:
    print(i,end=" ")
    
    if i not in x:
        x.append(i)
        print(i,end=" ")
    elif i not in y:
        print(i,end=" ")
        y.append(i)
        
        
print(x,end=" ")
print(y, end=" ")
        