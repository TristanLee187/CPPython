from sys import stdin
from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(10**4+1)
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    ans=0
    n,q=rns()
    tree=defaultdict(list)
    for i in range(n-1):
        a,b=rns()
        tree[a].append(b)
        tree[b].append(a)
    depths=[0 for i in range(n)]
    def dfs(curr, parent, depth):
        depths[depth] +=1
        for child in tree[curr]:
            if child != parent:
                dfs(child, curr, depth+1)
    dfs(1,-1,0)
    for i in range(q):
        scrap=rn()
    # print(depths)
    for i in range(n):
        if q<depths[i]:
            break
        ans+=depths[i]
        q-=depths[i]
    print('Case #' + str(_+1)+': ' + str(ans))