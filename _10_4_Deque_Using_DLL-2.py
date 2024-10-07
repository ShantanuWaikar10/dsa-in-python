class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next
        
class Deque:
    def __init__(self,start=None):
        self.start=start
        self.count_item=0
        
    def is_empty(self):
        return self.start==None
    
    def insert_front(self,data):
        n=Node(data,None,self.start)
        if self.start==None:
            self.start=n
        else:
            self.start.prev=n
            self.start=n
        self.count_item+=1
            
    def insert_rear(self,data):
        if self.start==None:
            n=Node(data,None,self.start)
            self.start=n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            n=Node(data,temp,None)
            temp.next=n
        self.count_item+=1
        
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        elif self.start.next is None:
            self.start=None
        else:
            self.start=self.start.next
        self.count_item-=1
            
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
        self.count_item-=1
            
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.start.item
        
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            return temp.item
        
    def size(self):
        return self.count_item          
    
q1=Deque()
q1.insert_rear(60)
q1.insert_front(20)
q1.insert_front(30)
q1.delete_front()
# q1.delete_rear()
print("front is",q1.get_front())
print("rear is",q1.get_rear())
print("size",q1.size())