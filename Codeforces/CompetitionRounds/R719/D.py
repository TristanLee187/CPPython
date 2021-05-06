from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import Counter

for _ in range(rn()):
    n=rn()
    a=rl()
    m=min(a)
    for i in range(n):
        a[i]-=m
    b=[]
    for i in range(n):
        b.append(a[i]-i)
    c=Counter(b)
    ans=0
    for i in c:
        ans+=c[i]*(c[i]-1)//2

    print(ans)