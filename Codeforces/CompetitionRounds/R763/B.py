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
    d=defaultdict(list)
    for i in range(n):
        a,b=rns()
        d[a].append(b)
    for key in d:
        d[key].sort()
        d[key].insert(0,key-1)
    ans=[]
    for key in sorted(d.keys()):
        for i in range(len(d[key])-1,0,-1):
            a,b,c=key,d[key][i],d[key][i-1]+1
            ans.append([a,b,c])
    for row in ans:
        print(*row)