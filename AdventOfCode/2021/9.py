prob="input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

ans=1
n=100
grid=[rs() for i in range(n)]
lows=[]
for i in range(n):
    for j in range(len(grid[0])):
        adj=[]
        if i>0:
            adj.append(grid[i-1][j])
        if i<n-1:
            adj.append(grid[i+1][j])
        if j>0:
            adj.append(grid[i][j-1])
        if j<len(grid[0])-1:
            adj.append(grid[i][j+1])
        if all([grid[i][j]<c for c in adj]):
            lows.append((i,j))
file.close()
# print(lows)

def bfs(i,j,num,lgrid):
    if grid[i][j] == '9':
        return 0
    adj = []
    if i > 0:
        adj.append((i - 1,j))
    if i < n - 1:
        adj.append((i + 1,j))
    if j > 0:
        adj.append((i,j-1))
    if j < len(grid[0]) - 1:
        adj.append((i,j+1))
    for c,b in adj:
        if int(grid[c][b])>num and int(grid[c][b])!=9 and lgrid[c][b]==0:
            lgrid[c][b]=1
            bfs(c, b, num + 1, lgrid)

vals=[]
for i,j in lows:
    localgrid = [[0 for k in range(len(grid[0]))] for l in range(n)]

    bfs(i,j,int(grid[i][j]), localgrid)
    vals.append(1+sum([s.count(1) for s in localgrid]))
vals.sort()
ans=vals[-1]*vals[-2]*vals[-3]
print(ans)
# print(vals)
