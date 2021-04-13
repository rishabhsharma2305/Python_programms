import sys
inf= sys.maxsize
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
visited[0]=True
while edges<4:
    minimum= sys.maxsize
    for i in range(5):
        if visited[i]:
            
            for j in range(5):
                if visited[j]==False and graph[i][j]<minimum:
                    minimum= graph[i][j]
                    a=i
                    b=j
    visited[b]=True
    cost+= graph[a][b]
    print(f"Edge found {a}-->{b}") 
    edges+=1
print("Total cost= ",cost)