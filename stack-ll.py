class node:
    def __init__(self,key):
        self.data= key
        self.next= None
class stacklinklist:
    def __init__(self):
        self.top= None
    def isempty(self):
        if self.top==None:
            return True
        return False
    def push(self,key):
        new_node= node(key)
        new_node.next= self.top
        self.top= new_node
    def pop(self):
        if self.isempty():
            print("stack epmty")
            return
        self.top= self.top.next
    def peek(self):
        if self.isempty():
            print("stack epmty")
            return
        return self.top.data
    def travarsal(self):
        if self.isempty():
            print("stack epmty")
            return
        temp= self.top
        while temp!=None:
            print(temp.data,end=" ")
            temp= temp.next
        print()
if __name__=='__main__':
    st= stacklinklist()
    st.travarsal()
    st.peek()
    st.pop()
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)
    st.travarsal()
    st.pop()
    st.travarsal()
    st.pop()
    st.travarsal()
    print()
    
