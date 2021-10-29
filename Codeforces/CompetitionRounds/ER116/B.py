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
    n,k=rns()
    n-=1
    ans=0
    add=1
    while n>0 and add<k:
        n-=add
        add*=2
        ans+=1
    if n>0:
        ans+=ceil_div(n,k)
    print(ans)