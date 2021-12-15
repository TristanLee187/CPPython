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
    n,k=rns()
    a=rl()
    a.sort()
    ans=0
    c=Counter(a[n-2*k:])
    for num in c:
        if c[num]>k:
            ans+=c[num]-k
            break
    for i in range(k):
        a.pop()
        a.pop()
    ans+=sum(a)
    print(ans)
