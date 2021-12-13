prob="input"

file=open(prob+".txt")

rn=lambda:int(line)
rns=lambda:map(int,line.split())
rl=lambda:list(map(int,line.split()))
rs=lambda:line.strip()

ans=0
lines = file.readlines()
n=len(lines)
file.close()
dots=847

maxx=0
maxy=0
p=[]
for i in range(dots):
    line=lines[i]
    x,y=map(int,rs().split(','))
    maxx=max(maxx,x)
    maxy=max(maxy,y)
    p.append((x,y))

grid = [[0 for i in range(maxx+1)] for j in range(maxy+1)]
for x,y in p:
    grid[y][x]=1

rs()
folds=[]
for i in range(dots+1, n):
    line=lines[i]
    folds.append(rs().split()[-1])

for i in range(len(folds)):
    fold=folds[i]
    axis=int(fold[2:])
    if fold[0]=='x':
        for j in range(len(grid)):
            rest=grid[j][axis+1:][::-1]
            pre=grid[j][:axis]
            for k in range(len(rest)):
                pre[-(k+1)] = max(pre[-k-1], rest[-k-1])
            grid[j]=pre.copy()
    else:
        for j in range(len(grid[0])):
            rest=[grid[a][j] for a in range(axis+1,len(grid))][::-1]
            pre=[grid[a][j] for a in range(axis)]
            for k in range(len(rest)):
                pre[-(k+1)] = max(pre[-k-1], rest[-k-1])
            for k in range(len(pre)):
                grid[k][j]=pre[k]
        for j in range(len(grid)-axis):
            grid.pop()
for row in grid:
    print(row)
print(ans)
