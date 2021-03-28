rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,u,v=rns()
    a=rl()
    ans=float('inf')
    for i in range(n-1):
        diff=a[i+1]-a[i]
        if abs(diff)>=2:
            ans=0
        elif abs(diff)==1:
            ans=min(ans,v,u)
        else:
            ans=min(ans,u+v,v+v)
    print(ans)
