

class stack: #define class named stack
    def __init__(self): #constructor
        #print('Hi')
        self.__stack_list = []
        
    def push(self, val):
        self.__stack_list.append(val)
        
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class AddingStack(stack): #subclass
    def __init__(self):
        stack.__init__(self)
        self.__sum = 0
        
    def get_sum(self):
        return self.__sum
        
    def push(self, val):
        self.__sum += val
        stack.push(self, val)
    
    def pop(self):
        val = stack.pop(self)
        self.__sum -= val
        return val
        
stack_obj = AddingStack() #initializing the objec
#print(len(stack_obj.__stack_list))
'''
stack_obj.push(3)
stack_obj.push(2)
stack_obj.push(1)

print(stack_obj.pop())
print(stack_obj.pop())
print(stack_obj.pop())
'''
for i in range(5):
    stack_obj.push(i)
print(stack_obj.get_sum())

for i in range(5):
    print(stack_obj.pop())