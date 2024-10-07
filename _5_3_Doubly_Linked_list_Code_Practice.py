class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
        
class DLL:
    def __init__(self,start=None):
        self.start = start
        
    def is_empty(self):
        return self.start==None
    
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n
        
    def insert_at_last(self,data):
        temp=self.start
        while temp.next is not None:
            temp=temp.next
        n=Node(temp,data,None)
        temp.next=n
        
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n
            
    def delete_first(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start==None
        else:
            self.start=self.start.next
            self.start.prev=None
            
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
            
    def delete_item(self,data):
        if self.is_empty():
            pass
        else:
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    if temp.prev is None:
                        self.start=temp.next
                        self.start.prev=None
                    elif temp.next is None:
                        temp.prev.next=None
                    else:
                        temp.prev.next=temp.next
                        temp.next.prev=temp.prev
                    break       
                temp=temp.next
        
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
            
mylist = DLL()
mylist.insert_at_start(5)
mylist.insert_at_start(6)
mylist.insert_at_start(7)

mylist.print_list()

# mylist.insert_at_last(10)

# mylist.insert_after(mylist.search(5),6)

# mylist.delete_first()

# mylist.delete_last()

mylist.delete_item(6)

print()
mylist.print_list()
