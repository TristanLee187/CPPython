from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

l=rs().split()
n,p=int(l[0]),float(l[1])

ans=1
while n:
    if n&1:
        ans=ans*(1-p)+(1-ans)*p
    p=p*(1-p)*2
    n//=2

print(ans)
