import copy

file=open("input.txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

n=137
grid=[list(rs()) for i in range(n)]
m=len(grid[0])
file.close()

ans=0
change=True
while change:
    change=False
    newgrid=copy.deepcopy(grid)
    for i in range(n):
        for j in range(m):
            if grid[i][j]=='>' and grid[i][(j+1)%m]=='.':
                change=True
                newgrid[i][j]='.'
                newgrid[i][(j+1)%m]='>'
    grid=copy.deepcopy(newgrid)
    for i in range(n):
        for j in range(m):
            if grid[i][j]=='v' and grid[(i+1)%n][j]=='.':
                change=True
                newgrid[i][j]='.'
                newgrid[(i+1)%n][j]='v'
    grid=newgrid
    if change:
        ans+=1

print(ans+1)
