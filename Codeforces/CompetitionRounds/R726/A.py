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
    s=sum(a)
    ans=0
    if s<n:
        ans=1
    elif s==n:
        ans=0
    else:
        ans=s-n
    print(ans)