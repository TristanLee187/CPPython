rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,u,r,d,l=rns()
    ans=True
    uo=max(0,u-n+2)
    ro = max(0, r-n+2)
    do= max(0, d-n+2)
    lo = max(0, l-n+2)
    if uo==2:
        r-=1
        l-=1
    if ro==2:
        u-=1
        d-=1
    if do==2:
        l-=1
        r-=1
    if lo==2:
        u-=1
        d-=1
    if uo==1:
        if r>l:
            r-=1
        else:
            l-=1
    if ro==1:
        if u>d:
            u-=1
        else:
            d-=1
    if lo==1:
        if u>d:
            u-=1
        else:
            d-=1
    if do==1:
        if l>r:
            l-=1
        else:
            r-=1
    ans=all([i>=0 for i in [u,l,r,d]])
    YN(ans)