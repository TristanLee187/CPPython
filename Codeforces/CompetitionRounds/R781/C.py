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
    a=rl()
    tree=defaultdict(list)
    for i in range(n-1):
        tree[a[i]].append(i+2)
    nums=[len(tree[i]) for i in tree]
    nums.append(1)
    nums.sort(reverse=True)
