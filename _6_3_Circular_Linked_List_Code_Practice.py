class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
        
class CLL:
    def __init__(self,last=None):
        self.last=last
        
    def is_empty(self):
        return self.last==None
    
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
                
    def print_list(self):
        if self.is_empty():
            pass
        else:
            temp=self.last.next
            while temp!=self.last:
                print(temp.item, end=" ")
                temp=temp.next
            print(temp.item)
            
    def insert_at_start(self,data):
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
        n=Node(data)
        if temp is not None:
            n.next=temp.next
            temp.next=n
            if temp==self.last: 
                self.last=n
                
    def delete_at_first(self):
        if self.is_empty():
            pass
        elif self.last==self.last.next:
            self.last=None
        else:
            self.last.next=self.last.next.next
            
    def delete_at_last(self):
        if self.is_empty():
            pass
        elif self.last==self.last.next:
            self.last=None
        else:
            temp=self.last
            while temp.next!=self.last:
                temp=temp.next
            temp.next=self.last.next
            self.last=temp
            
    def delete_item(self,data):
        if self.is_empty():
            pass
        elif self.last==self.last.next:
            if self.last.item==data:
                self.last=None
        elif self.last.next.item==data:
            self.delete_at_first()
        elif self.last.item==data:
            self.delete_at_last()
        else:
            temp=self.last.next
            while temp!=self.last:
                if temp.next.item==data:
                    temp.next=temp.next.next
                temp=temp.next
cll=CLL()
cll.insert_at_start(2)
cll.insert_at_last(10)
cll.insert_at_start(4)
cll.insert_at_last(9)
cll.insert_at_start(8)
# cll.insert_at_start(6)
# cll.insert_after(cll.search(10),3)
# cll.delete_at_first()
# cll.delete_at_last()
cll.print_list()
cll.delete_item(10)
cll.print_list()
