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
    n=rn()
    a=rl()
    a.sort()
    left=a[0]+a[1]
    right=a[-1]
    l=2
    r=n-2
    ans=False
    while r>l:
        if right>left:
            ans=True
            break
        left+=a[l]
        right+=a[r]
        l+=1
        r-=1
    if right > left:
        ans = True
    YN(ans)