class node:
    def __init__(self,key):
        self.data=key
        self.next=None


class linklist:
    def __init__(self):
        self.head=None

    # INSERTION AT BEGINING    
    def insert_at_begining(self,key):
        new_node= node(key)
        new_node.next= self.head
        self.head= new_node

    #INSERTION AT END
    def insert_at_end(self,key):
        new_node= node(key)
        if self.head==None:
            self.head= new_node
        else:
            temp= self.head
            while temp.next!=None:
                temp= temp.next
            temp.next= new_node

    #INSERTION AFTER A NODE
    def insert_after(self,after,key):
        if self.head== None:
            print("Link list empty")
        else:
            temp= self.head
            while temp!=None:
                if temp.data==after:
                    new_node= node(key)
                    new_node.next= temp.next
                    temp.next= new_node
                    return
                temp= temp.next
            if temp==None:
                print("No data found! as ",after)
        # else:
        #     temp= self.head
        #     while temp.data!= after:
        #         temp= temp.next
        #         if temp == None:
        #             print("no data found as ",after)
        #             return
        #     new_node= node(key)
        #     new_node.next= temp.next
        #     temp.next= new_node
    
    
    #DELETING A NODE
    def delete(self,key):
        if self.head.data==key:
            self.head= self.head.next
            return
        
        temp= self.head
        prev= temp
        while temp!=None:
            if temp.data==key:
                prev.next= temp.next
                return
            prev= temp
            temp= temp.next
        print(f"\nNo data found as {key} \n")

    
    #GETING NTH NODE FROM LAST
    
    def node_from_last(self,n):
        # ITRETIVE METHOD
        # if self.head==None:
        #     print("Link list empty")
        #     return
        # temp= self.head
        # length= 0
        # while temp!= None:
        #     temp= temp.next
        #     length+=1
        # temp= self.head
        # if length-n<0:
        #     print(f"no data found from last {n}")
        #     return
        # for i in range(length-n):
        #     temp= temp.next
        # print(f"{n}th node from last is {temp.data}")

        # TWO POINTER METHOD
        current= self.head
        prev= self.head
        for i in range(n):
            if current!=None:
                current= current.next
            else:
                print(f"no data found from last {n}")
                return
        while current!= None:
            prev= prev.next
            current= current.next
        print(f"{n}th node from last is {prev.data}")
    def print_list(self):
        temp= self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
        print()
my_list= linklist()
my_list.insert_at_begining(12)
my_list.insert_at_begining(15)
my_list.insert_at_begining(19)
my_list.print_list()
print()
my_list.insert_at_end(55)
my_list.insert_at_end(65)
my_list.print_list()
print()
my_list.insert_after(15,103)
my_list.insert_after(103,105)
my_list.insert_after(65,110)
my_list.insert_after(655,1110)
my_list.insert_after(19,500)
my_list.print_list()
print("\ndeleting elements\n")
my_list.delete(65)
my_list.delete(103)
my_list.delete(19)
my_list.print_list()
my_list.delete(11111)
my_list.print_list()
my_list.node_from_last(2)
my_list.node_from_last(5)
my_list.node_from_last(20)
my_list.node_from_last(6)
print()