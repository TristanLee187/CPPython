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
    ans=0
    m=1
    for i in range(n):
        while a[i]%2==0:
            m*=2
            a[i]=a[i]//2
        ans+=a[i]
    m*=max(a)
    ans-=max(a)
    print(ans+m)