rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,k=rns()
    s=rs()
    ans=False
    if k==0:
        ans=True
    else:
        ans=s[:k]==s[::-1][:k] and 2*k!=n
    YN(ans)