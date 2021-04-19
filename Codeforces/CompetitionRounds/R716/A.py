from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rl()
    ans=False
    for i in range(n):
        if int(a[i]**0.5)!=a[i]**0.5:
            ans=True
            break
    YN(ans)