from sys import stdin
from collections import defaultdict
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    n=rn()
    b=rl()
    p=rl()
    tree=defaultdict(list)
    root=-1
    for i in range(n):
        if b[i]!=i+1:
            tree[b[i]].append(i+1)
        else:
            root=b[i]
    if p[0]!=root:
        print(-1)
    else:
        paths=defaultdict(int)
        paths[root]=0
        ans=[0 for i in range(n)]
        for i in range(1,n):
            if b[p[i]-1] not in paths:
                ans=[-1]
                break
            ans[p[i]-1] = i-paths[b[p[i]-1]]
            paths[p[i]] = i
        print(*ans)
