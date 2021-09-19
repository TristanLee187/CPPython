from sys import stdin
from itertools import accumulate
from bisect import bisect_left
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rl()
    b=rl()
    maxes=list(accumulate(b,func=lambda a,b:max(a,b)))
    ans=float('inf')
    for i in range(n):
        poss=i+bisect_left(maxes,a[i])
        ans=min(ans,poss)
    print(ans)
