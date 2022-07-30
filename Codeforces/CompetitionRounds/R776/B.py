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
    l,r,a=rns()
    n=(r+1)//a
    x=n*a-1
    if l<=x<=r:
        pass
    else:
        x=r
    print(x//a + x%a)