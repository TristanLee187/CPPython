rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,m=rns()
    grid=[]
    for i in range(n):
        grid.append(rs())
    l=float('inf')
    r=0
    u=float('inf')
    d=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]=='1':
                l=min(l,i)
                r=max(r,i)
                u=min(u,j)
                d=max(d,j)
    ans=True
    for i in range(l,r+1):
        for j in range(u,d+1):
            if grid[i][j]=='0':
                ans=False
                break
    YN(ans)