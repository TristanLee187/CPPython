from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,m,k=rns()
    grid=[rs() for _ in range(n)]
    # print(grid)
    seen = [[0]*m for _ in range(n)]
    ans=True
    for row in range(n-1,-1,-1):
        for col in range(m):
            if grid[row][col]=='*':
                d=0
                i=1
                j=1
                new_cells=[]
                while row-i>=0 and col-j>=0 and col+j<m and grid[row-i][col-j]==grid[row-i][col+j]=='*':
                    d+=1
                    new_cells.append((row-i,col-j))
                    new_cells.append((row - i, col + j))
                    i+=1
                    j+=1
                if d>=k:
                    seen[row][col]=1
                    for r,c in new_cells:
                        seen[r][c]=1
                if not seen[row][col] and (d==0 or d<k):
                    # print(row,col)
                    ans=False
                    break
    YN(ans)