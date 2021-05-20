from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import defaultdict

for _ in range(rn()):
    n=rn()
    a=rl()
    d=defaultdict(int)
    ans=0
    for i in range(n):
        ans+=d[a[i]]*(n-i)
        d[a[i]]+=i+1
    print(ans)
