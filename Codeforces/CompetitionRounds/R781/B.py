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
    c=Counter(a)
    val=max(c.values())
    ans=n-val
    if ans!=0:
        for i in range(1,n):
            if val*(2**i) >= n:
                ans+=i
                break
    print(ans)