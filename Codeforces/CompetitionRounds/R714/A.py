from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from math import ceil

for _ in range(rn()):
    n,k=rns()
    if k==0:
        print(*list(range(1,n+1)))
    elif k>ceil((n-2)/2):
        print(-1)
    else:
        ans=n*[0]
        i=1
        for j in range(k):
            ans[i]=n-j
            i+=2
        i=1
        for j in range(n):
            if ans[j]==0:
                ans[j]=i
                i+=1
        print(*ans)