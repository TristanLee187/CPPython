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
    n,m=rns()
    grid=[rs() for i in range(n)]
    min_r=float('inf')
    min_c=float('inf')
    ans=True
    for i in range(n):
        for j in range(m):
            if grid[i][j]=='R':
                if (i<min_r and j>min_c) or (i>min_r and j<min_c):
                    ans=False
                    break
                else:
                    min_r=min(min_r, i)
                    min_c=min(min_c, j)
    YN(ans)
