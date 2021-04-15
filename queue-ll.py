class node:
    def __init__(self,val):
       self.data= val
       self.next= None

class queue:
    def __init__(self):
        self.front= None
        self.rear= None


    def enqueue(self, val):
        new_node= node(val)
        if self.front==None:
            self.front= new_node
            self.rear= new_node
            return
        self.rear.next= new_node
        self.rear= new_node


    def dequeue(self):
        if self.front==None:
            print("Empty")
            return
        self.front= self.front.next
        if self.front==None:
            self.rear= None
    def display(self):
        temp= self.front
        while temp!=None:
            print(temp.data,end=" ")
            temp= temp.next
        print()
if __name__=='__main__':
    q= queue()
    q.dequeue()
    q.enqueue(1)
    q.display()
    q.enqueue(2)
    q.display()
    q.enqueue(3)
    q.display()
    q.enqueue(4)
    q.display()
    q.enqueue(5)
    q.display()
    q.dequeue()
    q.display()
    q.dequeue()
    q.display()
    q.dequeue()
    q.display()
    q.dequeue()
    q.display()
    q.dequeue()
    q.display()
    q.dequeue()
    q.display()