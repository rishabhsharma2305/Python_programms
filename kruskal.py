import sys
inf= sys.maxsize
def matrix_to_list(mat):
    gr={}
    for i in range(len(mat)):
        gr[i]=[]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]!=inf:
                gr[i].append(j)
    return gr

graph=[
    [inf,2,inf,inf,3],
    [2,inf,3,4,inf],
    [inf,3,inf,4,inf],
    [inf,4,4,inf,5],
    [3,inf,inf,5,inf]
]
cost=0
# here, there are 5 vertices so 5-1= 4 edges would be needed
edges= 0
visited=[False]*5
parent=[0]*5
while edges<4:
    minimum= sys.maxsize
    for i in range(5):
        for j in range(5):
            if graph[i][j]<minimum:
                minimum= graph[i][j]
                a=i
                b=j
    x=a
    y=b
    while parent[x]!=0:
        x=parent[x]
    while parent[y]!=0:
        y= parent[y]
    if x!=y:
        print(f"node found {a}-->{b}")
        parent[b]=a
        edges+=1
        cost+=graph[a][b]
        graph[a][b]=graph[b][a]=inf # so that i won't select this edge again. 
print("cost= ",cost)
