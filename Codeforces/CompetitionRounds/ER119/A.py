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
    s=rs()
    n=s[:-1].count('N')
    if n==0:
        YN(s[-1]=='E')
    elif n==1:
        YN(s[-1]=='N')
    else:
        YN(True)