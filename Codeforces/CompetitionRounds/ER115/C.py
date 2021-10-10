from sys import stdin
from collections import Counter
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
    s=sum(a)
    b=[n*num-s for num in a]
    c=Counter(b)
    ans=0
    for i in range(n):
        ndiff=n*a[i]-s
        other=c[-ndiff]
        if ndiff==0:
            other-=1
        ans+=other
    print(ans//2)