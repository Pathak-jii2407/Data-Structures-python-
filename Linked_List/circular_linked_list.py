

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class CLL:
    def __init__(self,last=None):
        self.last=last

    def is_empty(self):
        return self.last==None
    
    def insert_at_first(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    def insert_after(self,temp,data):
        temp=self.last.next
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n

    def search(self,data):
        if self.is_empty():
            return None
        else:
            temp=self.last.next
            while temp!=self.last:
                if temp.item==data:
                    return temp
                temp=temp.next
            if temp.item==data:
                return temp
            return None        
    def print_all(self):
        if not self.is_empty():
            temp=self.last.next
            while temp!=self.last:
                print(temp.item)
                temp=temp.next
            print(temp.item)
    def delete_first(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next
        
    def delete_all(self):
        temp=self.last.next
        while self.last!=None:
            temp=temp.next
            self.last.next==None
    
            
    
    
    def delete_last(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                temp=self.last.next
                while temp.next!=self.last:
                    temp=temp.next
                if self.last.next==self.last:
                    temp=self.last.next
                temp.next=self.last.next
                self.last=temp
                
            
    
    def delete_item(self,data):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last.next=None
            else:
                if self.last.next.item==data:
                    mylist.delete_first()
                else:
                    temp=self.last.next
                    while temp!=self.last:
                        
                        if temp.next==self.last:
                            if self.last.item==data:
                                self.delete_last()
                        if temp.next.item==data:
                            temp.next=temp.next.next
                            break       
                        temp=temp.next
    def __iter__(self):
        if not self.is_empty():
            return CLLIterator(self.last.next)
        else:
            return CLLIterator(None)                
                     
class CLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count+=1
        data=self.current.item
        self.current=self.current.next
        return data
            


            


        
                    

mylist=CLL()

mylist.insert_at_last(10)
mylist.insert_at_last(0)
mylist.insert_at_first(9)
mylist.insert_at_first(8)
mylist.insert_at_first(6)
# mylist.insert_after(mylist.search(10),11)

# mylist.print_all()       
# mylist.delete_item(10)
# mylist.delete_all()
# mylist.delete_last()
# print('\n')
# mylist.print_all()

