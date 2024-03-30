

class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=start
        
    def insert_at_beg(self,data):
        n=Node(item=data,next=self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n
        
    def insert_at_last(self,data):
        temp=self.start
        n=Node(prev=temp,item=data)
        if not self.is_empty():
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
            
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None  
    def insert_at_middle(self,temp,data):
        if temp is not None:
            n=Node(prev=temp,item=data,next=temp.next)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n
    
    def is_empty(self):
        return self.start==None
    
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev==None

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp= self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
    def delete_any(self,data):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                    if temp.prev is not None:
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.next
                    break
                temp=temp.next

    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
    
    def __iter__(self):
        return DLLIterator(self.start)

class DLLIterator:
    def __init__(self,start):
        self.current=start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data

myList=DLL()
myList.insert_at_beg(10)
myList.insert_at_last(7)
myList.insert_at_middle(myList.search(7),15)
print('before deletion')
myList.print_list()

print('\nafter deletion')
myList.delete_first()
myList.delete_last()
myList.delete_any(7)
myList.print_list()

