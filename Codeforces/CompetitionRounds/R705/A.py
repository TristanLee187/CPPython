rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

from math import ceil

for _ in range(rn()):
    n,k=rns()
    ans=[]
    for i in range(1,n+1):
        if i>=ceil(k/2) and i!=k:
            ans.append(i)
    print(len(ans))
    print(*ans)