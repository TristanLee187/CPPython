from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    n,h=rns()
    a=rl()
    lo=1
    hi=h
    ans=h
    while lo<=hi:
        mid=(lo+hi)//2
        total=0
        right=a[0]
        for i in range(n):
            x,y=a[i],a[i]+mid
            total+=min(y-right,y-x)
            right=y
        if total<h:
            lo=mid+1
        else:
            ans=min(ans,mid)
            hi=mid-1
    print(ans)