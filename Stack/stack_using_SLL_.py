
from singly_linked_list import *

class Stack:
    def __init__(self):
        self.mylist=SLL()
        self.count=0
    def chk_empty(self):
        return self.mylist.is_empty()
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.count+=1
    def pop(self):
        if not self.chk_empty():
            self.mylist.delete_first()
            self.count-=1
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.chk_empty():
            return self.mylist.start.item
        else:
                raise IndexError("Stack is empty")
    def size(self):
        return self.count        
        


s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())

s1.pop()
print(s1.peek())
print("size: ",s1.size())
