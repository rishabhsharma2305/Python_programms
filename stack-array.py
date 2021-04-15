class stackarray:
    def __init__(self):
        self.top= -1
    max=5
    stack_lst=[]
    def isempty(self):
        if self.top<0:
            return True
        return False
    def isfull(self):
        if self.top>=self.max-1:
            return True
        return False
    def push(self,key):
        if self.isfull():
            print("stack overflow!")
            return
        self.top+=1
        self.stack_lst.append(key)     #self.stack_lst[top]=key
    def pop(self):
        if self.isempty():
            print("Stack empty!")
            return
        deleted_element= self.stack_lst[self.top]
        self.top-=1
        self.stack_lst.remove(deleted_element)
        return deleted_element
    def peek(self):
        if self.isempty():
            print("Stack empty!")
            return
        peek_element= self.stack_lst[self.top]
        return peek_element
    def traversal(self):
        if self.isempty():
            print("Stack empty!")
            return
        for i in range(0,self.top+1):
            print(self.stack_lst[i],end=' ')

if __name__=='__main__':
    stack1= stackarray()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)
    stack1.push(5)
    stack1.traversal()
    stack1.push(6)
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.traversal()
    print()
