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
    grid=[list(rs()) for __ in range(n)]
    li=0
    lj=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]=='L':
                li=i
                lj=j
                break
    cells=[]
    if li > 0 and grid[li - 1][lj] != '#':
        cells.append((li - 1, lj))
    if li < n - 1 and grid[li + 1][lj] != '#':
        cells.append((li + 1, lj))
    if lj > 0 and grid[li][lj - 1] != '#':
        cells.append((li, lj - 1))
    if lj < m - 1 and grid[li][lj + 1] != '#':
        cells.append((li, lj + 1))
    grid[li][lj]='+'
    while len(cells)>0:
        newcells=[]
        for i,j in cells:
            # seen[i][j]=True
            testcells=[]
            a=0
            if i > 0 and grid[i - 1][j] != '#':
                testcells.append((i - 1, j))
            if i < n - 1 and grid[i + 1][j] != '#':
                testcells.append((i + 1, j))
            if j > 0 and grid[i][j - 1] != '#':
                testcells.append((i, j - 1))
            if j < m - 1 and grid[i][j + 1] != '#':
                testcells.append((i, j + 1))
            for x,y in testcells:
                if grid[x][y]=='+':
                    a+=1
            if len(testcells)-a<=1:
                grid[i][j]='+'
                for x,y in testcells:
                    if grid[x][y]!='+':
                        newcells.append((x,y))
        cells=newcells
    grid[li][lj]='L'
    for row in grid:
        print(''.join(row))