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
    
    def search(self,data):
        temp=self.start
        if temp.item==data:
            return temp
        else:
            temp=temp.next
            while temp is not self.start:
                if temp.item==data:
                    return temp
                    break
                temp=temp.next
        return None
                
    def insert_at_start(self,data):
            n=Node()
            if self.is_empty():
                n.next=n
                n.item=data
                n.prev=n
                self.start=n
            else:
                n.next=self.start
                n.item=data
                n.prev=self.start.prev
                self.start.prev.next=n
                self.start.prev=n
                self.start=n
                
    def insert_at_last(self,data):
        n=Node()
        if self.is_empty():
            n.next=n
            n.item=data
            n.prev=n
            self.start=n
        else:
            n.next=self.start
            n.item=data
            n.prev=self.start.prev
            
            self.start.prev.next=n
            self.start.prev=n
            
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node()
            n.next=temp.next
            n.prev=temp
            n.item=data
            
            temp.next.prev=n
            temp.next=n
            
    def delete_first(self):
        if not self.is_empty():
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev=self.start.prev
                self.start=self.start.next
                
    def delete_last(self):
        if not self.is_empty():
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev
                
    def delete_item(self,data):
        if not self.is_empty():
            if self.start.item==data:
                self.delete_first()
            elif self.start.prev.item==data:
                self.delete_last()
            else:
                temp=self.start.next
                while temp != self.start.prev:
                    if temp.item==data:
                        temp.next.prev=temp.prev
                        temp.prev.next=temp.next
                    temp=temp.next
                
    def print_list(self):
            temp=self.start
            if not self.is_empty():
                print(temp.item,end=' ')
                temp=temp.next
                while temp is not self.start:
                    print(temp.item,end=' ')
                    temp=temp.next  
                
                
mylist=CDLL()
mylist.insert_at_start(2)
mylist.insert_at_start(4)
mylist.insert_at_last(5)
mylist.insert_after(mylist.search(5),9)
# mylist.delete_first()
# mylist.delete_last()
mylist.delete_item(5)
mylist.print_list()