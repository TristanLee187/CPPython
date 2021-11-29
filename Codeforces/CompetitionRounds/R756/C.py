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
    if a[0]==n:
        ans=[n]+a[1:][::-1]
    elif a[-1]==n:
        ans=a[:-1][::-1]+[n]
    else:
        ans=[-1]
    print(*ans)