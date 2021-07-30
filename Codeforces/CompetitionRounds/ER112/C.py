from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from itertools import accumulate

for _ in range(rn()):
    n=rn()
    top=rl()
    bottom=rl()
    if n==1:
        print(0)
    else:
        top=list(accumulate(top[::-1]))[::-1]
        bottom=list(accumulate(bottom))
        ans=float('inf')
        for i in range(1,n):
            if i==1:
                ans=min(ans,top[i])
            else:
                ans=min(ans, max(top[i], bottom[i-2]))
        ans=min(ans, bottom[-2])
        print(ans)