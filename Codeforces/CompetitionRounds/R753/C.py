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
    acc=a[0]
    ans=a[0]
    for i in range(1,n):
        ans = max(ans, a[i]-acc)
        acc=a[i]
    print(ans)