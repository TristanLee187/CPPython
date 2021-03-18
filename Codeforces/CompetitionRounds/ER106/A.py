rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,k1,k2=rns()
    w,b=rns()
    ans=w<=min(k1,k2) + abs(k2-k1)//2
    ans=ans and b<=min(n-k1,n-k2)+ abs(k2-k1)//2
    YN(ans)