
class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class CDLL:
    def __init__(self,start=None):
        self.start=start
    
    def is_empty(self):
        return self.start==None
    def insert_at_begin(self,data):
        n=Node(item=data)
        if self.is_empty():
            n.next=n
            n.prev=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
        self.start=n
    def insert_at_last(self,data):
        n=Node(item=data)
        if self.is_empty():
            n.next=n
            n.prev=n
            self.start=n
        else:
            n.prev=self.start.prev
            n.next=self.start
            n.prev.next=n
            self.start.prev=n
    
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(item=data)
            n.next=temp.next
            n.prev=temp
            temp.next.prev=n
            temp.next=n            
    
    def search(self,data):
        temp=self.start
        if self.is_empty():
            return None
        if temp.item==data:
            return temp
        else:
            temp=temp.next
            while temp!=self.start:
                if data==temp.item:
                    return temp
                temp=temp.next
            return None
    
    def Print(self):
        temp=self.start
        if not self.is_empty():
            print(temp.item,end=' ')
            temp=temp.next
            while self.start!=temp:
                print(temp.item,end=' ')
                temp=temp.next
    
    def delete_first(self):
        if not self.is_empty():
            if self.start.next==self.start.prev:
                self.start=None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev=self.start.prev
                self.start=self.start.next
    
    def delete_last(self):
         if not self.is_empty():
            if self.start.next==self.start.prev:
                self.start=None
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev
    def delete_item(self,data):
        if not self.is_empty():
            temp=self.start
            if temp.item==data:
                self.delete_first()
            elif temp.prev.item==data:
                self.delete_last()
            else:
                temp=temp.next
                while temp is not self.start:
                    if temp.item==data:
                        temp.next.prev=temp.prev
                        temp.prev.next=temp.next
                    temp=temp.next
    
    def __iter__(self):
        return CDLLiterator(self.start)

class CDLLiterator:
    def __init__(self,start):
        self.current=start
        self.count=0
        self.start=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current ==None:
            raise StopIteration
        if self.count==self.start and  self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        return data
        
            
        
mylist=CDLL()


mylist.insert_at_begin(1)
mylist.insert_at_last(3)
mylist.insert_at_last(4)
mylist.insert_at_last(5)
mylist.insert_after(mylist.search(1),2)

mylist.Print()

print('\n\nAfter Delete')
mylist.delete_item(2)
mylist.Print()

# for x in mylist:
#     print(x,end=' ')


