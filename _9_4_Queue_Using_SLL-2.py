class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
        
class Queue:
    def __init__(self,start=None):
        self.start=start
        self.count_items=0
        
    def is_empty(self):
        return self.start==None
    
    def enqueue(self,data):
        n=Node(data,self.start)
        self.start=n
        self.count_items+=1
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        elif self.start.next==None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
        self.count_items-=1
        
    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        temp=self.start
        while temp.next is not None:
            temp=temp.next
        return temp.item
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.start.item
    
    def size(self):
        return self.count_items
            
            
try:
    q1=Queue()
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    q1.dequeue()
    print("Front is",q1.get_front())
    print("Rear is",q1.get_rear())
    print("Size is",q1.size())
    
except IndexError as e:
    print(e.args[0])