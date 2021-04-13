import sys
inf= sys.maxsize
graph=[
    [0,2,4,inf,inf,inf],
    [inf,inf,1,7,inf,inf],
    [inf,inf,inf,inf,3,inf],
    [inf,inf,inf,inf,inf,1],
    [inf,inf,inf,2,inf,5],
    [inf,inf,inf,inf,inf,inf]
]
visited=[False]*6
parent=[0]*6
dist=[]
count=0
visited[0]=True
for i in range(6):
    dist.append(graph[0][i])
while count<6:
    min_dist= inf
    # for finding vertex of minimum distance
    for i in range(6):
        if visited[i]==False and dist[i]<min_dist:
            min_dist=dist[i]
            next_node=i
    visited[next_node]= True
    # relaxing all other vertices from founded vertex
    for i in range(6):
        if min_dist+graph[next_node][i]<dist[i]:
            dist[i]= min_dist+graph[next_node][i]
            parent[i]=next_node
    count+=1
for i in range(6):
    print(f"\nminimum distance of {i+1} = {dist[i]}")
    print(f"path of {i+1}",end=" ")
    j=i
    while True:
        j=parent[j]
        print(f"<---{j+1}",end="")
        if j==0:
            break