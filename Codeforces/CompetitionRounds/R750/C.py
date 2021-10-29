from sys import stdin
from collections import defaultdict
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    s=rs()
    ans=float('inf')
    for char in set(s):
        l,r=0,n-1
        pans=0
        while l<r:
            # print(char, pans)
            if s[l]==s[r]:
                l+=1
                r-=1
            elif s[l]==char:
                l+=1
                pans+=1
            elif s[r]==char:
                r-=1
                pans+=1
            else:
                pans=float('inf')
                break
        ans=min(ans,pans)
    if ans==float('inf'):
        print(-1)
    else:
        print(ans)