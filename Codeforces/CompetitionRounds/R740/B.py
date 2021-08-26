from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from math import ceil

for _ in range(rn()):
    a,b=rns()
    n=a+b
    ans=set()
    def f(ans,c,d):
        mi=abs(a-c)
        ma=min(a,d)+min(b,c)
        for i in range(mi,ma+1,2):
            ans.add(i)
    f(ans,n//2,ceil(n/2))
    f(ans,ceil(n/2),n//2)
    ans=sorted(list(ans))
    print(len(ans))
    print(*ans)
