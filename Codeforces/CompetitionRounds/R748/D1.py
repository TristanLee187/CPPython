from sys import stdin
from math import gcd
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
    diff=[a[i]-a[i-1] for i in range(1,n)]
    diff=[num for num in diff if num!=0]
    if len(diff)==0:
        print(-1)
    else:
        ans=diff[0]
        for num in diff:
            ans=gcd(ans,num)
        print(ans)