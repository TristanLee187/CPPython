rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    p,a,b,c=rns()
    ans=(a-(p%a))%a
    ans=min(ans,(b-(p%b))%b)
    ans=min(ans,(c-(p%c))%c)
    print(ans)