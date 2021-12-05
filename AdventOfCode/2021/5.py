prob="input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

ans=0
n=500
grid=[[0 for i in range(1000)] for j in range(1000)]
for i in range(n):
    a,b=rs().split('->')
    x1,y1=map(int,a.split(','))
    x2,y2=map(int,b.split(','))
    if x1==x2:
        for j in range(min(y1,y2),max(y1,y2)+1):
            grid[x1][j]+=1
    elif y1==y2:
        for j in range(min(x1,x2),max(x1,x2)+1):
            grid[j][y1]+=1
    else:
        sx=-1 if x1>x2 else 1
        sy = -1 if y1>y2 else 1
        for j in range(abs(x2-x1)+1):
            grid[x1+j*sx][y1+j*sy]+=1

for row in grid:
    for num in row:
        if num>=2:
            ans+=1
file.close()

print(ans)
