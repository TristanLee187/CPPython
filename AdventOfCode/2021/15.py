from collections import defaultdict
from heapq import heappop, heappush


def dijkstra(graph, start):
    """
        Uses Dijkstra's algortihm to find the shortest path from node start
        to all other nodes in a directed weighted graph.
    """
    n = len(graph)
    dist, parents = [float("inf")] * n, [-1] * n
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len == dist[v]:
            for w, edge_len in graph[v]:
                if edge_len + path_len < dist[w]:
                    dist[w], parents[w] = edge_len + path_len, v
                    heappush(queue, (edge_len + path_len, w))

    return dist, parents

prob="input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

ans=0
n=100
grid=[list(map(int, rs())) for i in range(n)]
# Read input, account for sample vs. actual input
file.close()
actualgrid=[]
for i in range(5):
    for row in grid:
        newrow=[k+i for k in row]
        for j in range(len(newrow)):
            if newrow[j]>9:
                newrow[j]-=9
        prev=newrow.copy()
        for j in range(4):
            add=[k+1 if k<9 else 1 for k in prev]
            newrow+=add
            prev=add.copy()
        actualgrid.append(newrow)

graph=defaultdict(list)
for i in range(5*n):
    for j in range(5*n):
        adj=[]
        if i>0:
            adj.append((i-1,j))
        if i<5*n-1:
            adj.append((i+1,j))
        if j>0:
            adj.append((i,j-1))
        if j<5*n-1:
            adj.append((i,j+1))

        for x,y in adj:
            graph[5*n*i+j].append((5*n*x+y, actualgrid[x][y]))

a=dijkstra(graph, 0)
# for row in actualgrid:
#     print(row)
print(a[0][-1])