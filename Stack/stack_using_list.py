
class Stack:
    def __init__(self):
        self.item=[]
    def is_empty(self):
        return len(self.item)==0
    def push(self,data):
        self.item.append(data)
        
    def pop(self):
        if not self.is_empty():
            return self.item.pop() 
        else:
            raise IndexError("Stack Is Empty")
            
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("Stack Is Empty")
    def size(self):
        return len(self.item)
    
    def print_all(self):
        p=0
        l=len(self.item)
        while p!=l:
            print(self.item[p])
            p+=1

stack=Stack()
print(stack.is_empty())
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(10)
print(stack.is_empty())

stack.print_all()

print('\n'*5)

stack.pop()
stack.print_all()

print('\n'*5)
print(stack.peek())

print('\n'*5)

print(stack.size())
