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
    rs()
    m,n=rns()
    grid=[rl() for i in range(m)]
    lo=1
    hi=10**9
    ans=1
    while lo<=hi:
        mid=(lo+hi)//2
        s=set()
        need=0
        br=False
        for i in range(n):
            good=[j for j in range(m) if grid[j][i]>=mid]
            if len(good)==0:
                br=True
                break
            f=False
            for num in good:
                if num in s:
                    f=True
                    break
                s.add(num)
            if not f:
                need+=1
        if need<n and not br:
            ans=max(ans,mid)
            lo=mid+1
        else:
            hi=mid-1
    print(ans)

