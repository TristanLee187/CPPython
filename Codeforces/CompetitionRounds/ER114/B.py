from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    a,b,c,m=rns()
    a,b,c=sorted([a,b,c],reverse=True)
    ma=a+b+c-3
    mi=a-b-1
    mi=max(0,mi-c)
    YN(mi<=m<=ma)
