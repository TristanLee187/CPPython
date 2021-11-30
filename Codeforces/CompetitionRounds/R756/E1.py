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
    rs()
    n,k=rns()
    friends=rl()
    tree=defaultdict(set)
    for __ in range(n-1):
        x,y=rns()
        tree[x].add(y)
        tree[y].add(x)
    leaves = [i for i in range(1,n+1) if len(tree[i])==1]
