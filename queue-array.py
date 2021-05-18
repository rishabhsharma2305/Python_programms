class queue:
    size= 10
    queue= [None]*size
    def __init__(self):
        self.front= -1
        self.rear= -1


    def isempty(self):
        if self.front==-1:
            return True
        else:
            return False


    def isfull(self):
        if self.rear==self.size-1 and self.front==0:
            return True
        if self.rear==self.front-1:         # since we are assuming it to be circular queue
            return True
        return False


    def enqueue(self, val):
        if self.isfull():
            print("Queue is full")
            return
        elif self.isempty():
            self.front= 0
            self.rear= 0
            self.queue[self.rear]= val  # we can also use queue.append but that will fail in case of circular queue
        else:
            self.rear= (self.rear+1)%self.size
            self.queue[self.rear]= val


    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return
        if self.front==self.rear:
            self.front= -1
            self.rear= -1
        self.front= (self.front+1)%self.size


    def print_queue(self):
        if self.front < self.rear:
            for i in range(self.front,self.rear+1):
                print(self.queue[i], end=" ")
        elif self.front > self.rear:
            for i in range(self.rear,self.front+1):
                print(self.queue[i], end=" ")
        else:
            print(self.queue[self.front])
        print()

if __name__=='__main__':
    q= queue()
    q.enqueue(1)
    q.print_queue()
    q.enqueue(2)
    q.print_queue()
    q.enqueue(3)
    q.print_queue()
    q.enqueue(4)
    q.print_queue()
    q.enqueue(5)
    q.print_queue()
    q.enqueue(6)
    q.print_queue()
    q.enqueue(7)
    q.print_queue()
    q.enqueue(8)
    q.print_queue()
    q.enqueue(9)
    q.print_queue()
    q.enqueue(10)
    q.print_queue()
    q.enqueue(11)
    q.print_queue()
    q.enqueue(12)
    q.print_queue()
    q.dequeue()
    q.print_queue()
    q.dequeue()
    q.print_queue()
    q.dequeue()
    q.print_queue()
    q.dequeue()
    q.print_queue()
    q.dequeue()
    q.print_queue()
    q.enqueue(11)
    q.print_queue()
    q.enqueue(12)
    q.print_queue()
    q.dequeue()
    q.print_queue()
    q.dequeue()
    q.print_queue()
    q.dequeue()
    q.print_queue()
    q.dequeue()
    q.print_queue()
    q.dequeue()
    q.print_queue()
    q.dequeue()
    q.print_queue()
    print()