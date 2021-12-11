prob="input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

ans=0
n=10
grid=[list(map(int,rs())) for i in range(n)]
def bfs(currgrid,seen):
    adj = []
    for i in range(n):
        for j in range(n):
            adj.append((i,j))
    while len(adj)>0:
        new_adj = []
        for i,j in adj:
            if (i,j) not in seen:
                currgrid[i][j]+=1
                if currgrid[i][j] > 9:
                    seen.add((i, j))
                    for k in range(-1,2):
                        for m in range(-1,2):
                            if (k!=0 or m!=0) and 0<=i+k<n and 0<=j+m<n and (i+k, j+m) not in seen:
                                new_adj.append((i+k, j+m))
        adj=new_adj.copy()
        # print(adj)
        # for row in new_grid:
        #     print(row)
    for i,j in seen:
        currgrid[i][j]=0

found=False
step=0
while not found:
    new_grid = grid.copy()
    seen=set()
    bfs(new_grid,seen)
    grid = new_grid.copy()
    step+=1
    founda=True
    for i in range(n):
        for j in range(n):
            if grid[i][j]!=0:
                founda=False
                break
    found=founda
file.close()

# print(ans)
print(step)
