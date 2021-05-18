from collections import deque
class graph:
    adj_list={}  # this is graph {vertex:[list vertices connected to it] }
    vertices=0

    # constructer for creating a graph
    def __init__(self,vertices,edges):
        self.vertices= vertices
        for i in range(1,self.vertices+1):
            self.adj_list[i]=[]
        for i in edges:
            self.adj_list[i[0]].append(i[1])        #because if 1 contain 2 then visa verse must be true
            self.adj_list[i[1]].append(i[0])    
    def print_graph(self):
        for i,j in self.adj_list.items():
            print(i," ",j) 
    def bfs(self, source, v):
        visited= [False]*(v+1)
        que= deque()
        que.append(source)
        visited[source]= True
        bfs_ans=[]
        while len(que)!=0:
            current= que.popleft()
            bfs_ans.append(current)
            for vertex in self.adj_list[current]:
                if visited[vertex]==False:
                    visited[vertex]= True
                    que.append(vertex)
        return bfs_ans
    
    # this method will do in depth of the node given
    def dfs_util(self,source,dfs_ans,visited):
        visited[source]= True
        dfs_ans.append(source)
        for vertex in self.adj_list[source]:
            if visited[vertex]==False:
                self.dfs_util(vertex,dfs_ans,visited)

    def dfs(self, source, v):
        visited= [False]*(v+1)
        dfs_ans=[]
        self.dfs_util(source, dfs_ans, visited)
        return dfs_ans


if __name__=='__main__':
    vertices= 4
    edges= [ [1,2] , [1,3] , [1,4] , [2,4] , [3,4] ] #list of edges. [1,2]---> edge between 1 and 2
    gr= graph(vertices,edges)
    gr.print_graph()
    bfs_traversal= gr.bfs(1,vertices)
    print(bfs_traversal)
    dfs_traversal= gr.dfs(1,vertices)
    print(dfs_traversal)
    print()