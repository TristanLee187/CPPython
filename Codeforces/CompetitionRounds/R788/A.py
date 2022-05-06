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
    neg=len([i for i in range(n) if a[i]<0])
    a=[abs(a[i]) for i in range(n)]
    for i in range(n):
        if a[i]>0 and neg>0:
            a[i]*=-1
            neg-=1
    ans=True
    for i in range(n-1):
        if a[i]>a[i+1]:
            ans=False
            break
    YN(ans)