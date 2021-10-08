from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,k=rns()
    ans=0
    c=0
    while k:
        ans+=pow(n,c,mod)*(k%2)
        ans%=mod
        k//=2
        c+=1
    print(ans)