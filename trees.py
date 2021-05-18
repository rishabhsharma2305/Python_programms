from collections import deque
class node:
    def __init__(self,val):
        self.val= val
        self.left= None
        self.right= None
class binarytree:
    def __init__(self):
        self.root= None
    
    def preorder(self,root):
        if root==None:
            return
        print(root.val, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)
    def postorder(self,root):
        if root==None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val, end=" ")

    def bfs(self,root):
        if root==None:
            return
        q= deque()
        q.append(root)
        res=[]
        while len(q)!=0:
            currentlevel=[]
            n= len(q)
            for i in range(n):
                curr_node= q.popleft()
                currentlevel.append(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            res.append(currentlevel)  
        return res
    def dfs(self,root):
        if root==None:
            return
        q= deque()
        q.append(root)
        res=[]
        while len(q)!=0:
            currentlevel=[]
            n= len(q)
            for i in range(n):
                curr_node= q.pop()
                currentlevel.append(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            res.append(currentlevel)  
        return res


    def length(self,root):
        if root==None:
            return 0
        return 1+ self.length(root.left)+self.length(root.right)

    def max_tree(self,root):
        high= -10000
        if root!=None:
            left= self.max_tree(root.left)
            right= self.max_tree(root.right)
            curr= root.val
            high= max(left,right,curr)
        return high
        
    def search(self,root,data):
        if root==None:
            return False
        if root.val==data:
            return True
        temp= self.search(root.left,data)
        if temp==True:
            return True
        else:
            return self.search(root.right,data)
    
    def height(self,root):
        if root==None:
            return -1
        left= self.height(root.left)
        right= self.height(root.right)
        return max(left,right)+1

    def leave(self,root):
        if root==None:
            return 0
        
        if root.left!=None or root.right!=None:
            left= self.leave(root.left)
            right= self.leave(root.right)
            return left+right
        return 1

    def fullnodes(self,root):
        if root==None:
            return 0
        if root.left==None or root.right==None:
            return 0
        left= self.fullnodes(root.left)
        right= self.fullnodes(root.right)
        return left+right+1
    
if __name__=='__main__':
    tree= binarytree()
    tree.root= node(1)
    tree.root.left= node(2)
    tree.root.right= node(3)
    tree.root.left.left= node(4)
    tree.root.left.right= node(5)
    tree.root.right.left= node(6)
    tree.root.right.right= node(7)
    print("\nPreorder: ")
    tree.preorder(tree.root)
    print("\ninorder: ")
    tree.inorder(tree.root)
    print("\npostorder: ")
    tree.postorder(tree.root)
    print("\nBFS: ")
    print(tree.bfs(tree.root))
    print("\nDFS: ")
    print(tree.dfs(tree.root))
    print("\n length: ",tree.length(tree.root))
    print("\n max in tree: ",tree.max_tree(tree.root))
    print("\n 6 exist in tree",tree.search(tree.root,6))
    print("\n 5 exist in tree",tree.search(tree.root,5))
    print("\n 4123 exist in tree",tree.search(tree.root,4123))
    print("\n height of tree: ",tree.height(tree.root))
    print("\n leave nodes of tree: ",tree.leave(tree.root))
    print("\n full nodes of tree: ",tree.fullnodes(tree.root))
    print()


