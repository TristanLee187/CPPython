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
    ans=False
    if n%2==0:
        if (n//2)**0.5==int((n//2)**0.5):
            ans=True
    if n%4==0:
        if (n//4)**0.5 == int((n//4)**0.5):
            ans=True

    YN(ans)