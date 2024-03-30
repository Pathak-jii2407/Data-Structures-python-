
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next


class Stack:
    def __init__(self):
        self.start=None
        self.item_cout=0
    
    def is_empty(self):
        return self.start==None
     
    def push(self,data):  
        n=Node(data,self.start)   
        self.start=n   
        self.item_cout+=1
        
    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next
            self.item_cout-=1
            return data
        else:
            raise IndexError("Stack is empty")
        
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError(self.is_empty())
    def size(self):
        return self.item_cout
    def Print(self):
        temp=self.start
        i=0
        while temp!=None:
            i+=1
            print(f" {i} > {temp.next} item is {temp.item}")
            temp=temp.next
            
        
        
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
s1.push(60)
s1.push(70)
print("size",s1.size())
print("peek: ",s1.peek())
print('\n'*5,end="After Deletion\n")
s1.pop()
print("size",s1.size())
print("peek: ",s1.peek())
# s1.Print()

