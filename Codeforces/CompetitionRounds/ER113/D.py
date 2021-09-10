from sys import stdin
import bisect
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,m,k=rns()
    x=sorted(rl())
    y=sorted(rl())
    p=[tuple(rns()) for __ in range(k)]
    xs=sorted([p[i][0] for i in range(k)])
    ys=sorted([p[i][1] for i in range(k)])
    ans=0
    for i in range(n-1):
        l,r=x[i]+1,x[i+1]-1
        j=bisect.bisect_left(xs,l)
        k=bisect.bisect_right(xs,r)
        d=k-j
        # print(d)
        ans+=max((d-1)*d//2,0)
    for i in range(m-1):
        l,r=y[i]+1,y[i+1]-1
        j=bisect.bisect_left(ys,l)
        k=bisect.bisect_right(ys,r)
        d=k-j
        # print(d)
        ans+=max((d-1)*d//2,0)
    print(ans)
