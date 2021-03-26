rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,m,x=rns()
    a=x//n
    if a*n==x:
        a-=1
    b=x%n
    if b==0:
        b=n
    print((b-1)*m+a+1)