from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().strip().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from math import ceil

for _ in range(rn()):
    n=rn()
    a=sorted(rl())
    b=sorted(rl())
    low=0
    high=n
    ans=float('inf')
    while low<=high:
        mid=(low+high)//2
        take=ceil(3*(n+mid)/4)
        c=mid*100+sum(a[n-(take-mid):])
        d=sum(b[max(n-take,0):])
        if c>=d:
            ans=min(ans,mid)
            high=mid-1
        else:
            low=mid+1
    print(ans)