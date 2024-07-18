# file = open('new.txt','w')
# file.write('Put in my stuff the way I like em. This is my safe python space')





# file = open('new.txt','a')
# file.write(" Y'all deal with it." )
# file.close()

# file = open('new.txt', 'r')
# print(file.read())
# file.close()

# import os
# if os.path.exists("new.txt"):
#   os.remove("new.txt")
# else:
#   print("The file does not exist")


# def subtract(a,b):
#     return(a - b)

# c = subtract

# def extendSubtract(func:subtract, a,b,c):
#     result = func(a,b)
#     return(c * result)

# print(extendSubtract(subtract,5,2,2))



from mymodule import mylist
print(mylist([0],[1]))