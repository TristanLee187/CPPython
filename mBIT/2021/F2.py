from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import defaultdict

n=rn()
graph=defaultdict(set)
outs=defaultdict(set)
for i in range(n-1):
    u,v=rns()
    graph[u].add(v)
    graph[v].add(u)
    outs[u].add(v)
    outs[v].add(u)

members=defaultdict(int)
counts=defaultdict(set)

for num in graph:
    members[num]=len(graph[num])
    counts[len(graph[num])].add(num)

backlog=defaultdict(list)
while len(counts[1])>0:
    next=set()
    for num in counts[1]:
        if len(graph[num])>0:
            child=graph[num].pop()
            print(child,num)
            backlog[num].append(child)
            graph[child].remove(num)
            members[child]-=1
            if members[child]==0 and child in next:
                next.remove(child)
            elif members[child]==1:
                next.add(child)
            else:
                counts[members[child]].add(child)

    counts[1]=next.copy()

# print(backlog)


def dfs(backlog,num,seen):
    if backlog[num][0] not in backlog or len(backlog[backlog[num][0]])==0:
        print(num,backlog[num][0])
        seen[num]=True
        backlog[num].pop()
    else:
        dfs(backlog,backlog[num][0],seen)
        print(num,backlog[num][0])
        seen[num] = True
        backlog[num].pop()

seen=(n+1)*[False]
for i in backlog:
    if not seen[i]:
        dfs(backlog,i,seen)

