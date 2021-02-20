rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))

# Python program to print all paths from a source to destination.

from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.paths=[]

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'. 
    visited[] keeps track of vertices in current path. 
    path[] stores actual vertices and path_index is current 
    index in path[]'''

    def printAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            self.paths.append(path.copy())
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)

                # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False] * (self.V)

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)

    # Create a graph given in the above diagram

# This code is contributed by Neelam Yadav

n,m,x,y=rns()
g=Graph(n+1)
roads={}
for i in range(m):
    road=rl()
    roads[(road[0],road[1])]=[road[2],road[3]]
    roads[(road[1], road[0])] = [road[2], road[3]]
    g.addEdge(road[0],road[1])
    g.addEdge(road[1],road[0])
g.printAllPaths(x,y)
ans=float('inf')
for path in g.paths:
    acc=0
    for i in range(len(path)-1):
        val=roads[(path[i],path[i+1])]
        acc+=(val[1]-acc%(val[1]))%val[1]
        acc+=val[0]
    ans=min(ans,acc)
if ans==float('inf'):
    print(-1)
else:
    print(ans)
print(g.paths)