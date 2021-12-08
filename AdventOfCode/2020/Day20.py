from collections import defaultdict

prob="input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

ans=1
tiles={}
n=144
for i in range(n):
    s=rs().split()
    tile = int(s[1][:-1])
    tiles[tile] = [rs() for j in range(10)]
    rs()

strings=defaultdict(int)
string_to_grid = defaultdict(list)
for grid in tiles.values():
    s1=''.join(grid[0])
    s2=''.join([grid[i][0] for i in range(10)])
    s3 = ''.join([grid[i][-1] for i in range(10)])
    s4=''.join(grid[-1])
    for s in [s1,s2,s3,s4]:
        strings[s]+=1
        strings[s[::-1]]+=1
        string_to_grid[s].append(grid)
        string_to_grid[s[::-1]].append(grid)
file.close()
corners=[]
orient=[]
for num in tiles:
    grid=tiles[num]
    s1=''.join(grid[0])
    s2=''.join([grid[i][0] for i in range(10)])
    s3 = ''.join([grid[i][-1] for i in range(10)])
    s4=''.join(grid[-1])
    a=0
    o=[]
    for i in range(4):
        s=[s1,s2,s3,s4][i]
        if strings[s]==1:
            a+=1
            o.append(i)
    if a==2:
        ans*=num
        corners.append(num)
        orient.append(o)

image = [[[] for i in range(12)] for j in range(12)]
print(orient)

print(ans)
