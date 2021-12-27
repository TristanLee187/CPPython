from sys import stdin
from itertools import accumulate

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
    s=sum(a)
    a.sort()
    diff=[a[i]-a[0] for i in range(1,n)]
    diff.reverse()
    suff=list(accumulate(diff))
    suff.reverse()
    suff.append(0)
    # print(suff)
    def solve():
        need=s-k
        if need<=0:
            return 0
        ans=float('inf')
        for i in range(1,n+1):
            b=suff[-i]
            pans=ceil_div(max(0,need-b),i)+i-1
            ans=min(ans,pans)
            # print(i,pans)
        return ans
    print(solve())