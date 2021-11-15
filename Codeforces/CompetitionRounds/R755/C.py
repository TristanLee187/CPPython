from sys import stdin
from collections import Counter
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
    b=rl()
    a.sort()
    b.sort()
    ans=True
    for i in range(n):
        d=b[i]-a[i]
        if d not in [0,1]:
            ans=False
            break
    YN(ans)
