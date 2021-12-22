file=open("input.txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

n=420
ans=0
cuboids=[]
def seginter(a,b,c,d):
    res = -(max(a,c)-min(b,d))
    if res<0:
        return False
    return [max(a,c), min(b,d)]
def inter(cube1, cube2):
    xa1,xb1,ya1,yb1,za1,zb1 = cube1[1:]
    xa2, xb2, ya2, yb2, za2, zb2 = cube2[1:]
    x=seginter(xa1,xb1,xa2,xb2)
    y = seginter(ya1, yb1, ya2, yb2)
    z = seginter(za1, zb1, za2, zb2)
    if x and y and z:
        return [1]+x+y+z
    return False
def vol(cube):
    xa1, xb1, ya1, yb1, za1, zb1 = cube[1:]
    return abs((xb1-xa1+1)*(yb1-ya1+1)*(zb1-za1+1))

for __ in range(n):
    line=rs().split()
    set=0 if line[0]=='off' else 1
    coors=line[1].split(',')
    xa,xb=map(int,coors[0][2:].split('..'))
    ya,yb = map(int,coors[1][2:].split('..'))
    za,zb = map(int,coors[2][2:].split('..'))
    cuboids.append([set,xa,xb,ya,yb,za,zb])
file.close()

cuboids.reverse()
total=[]
for cube in cuboids:
    add=[]
    for other in total:
        sec = inter(cube, other[:-1])
        if sec:
            if cube[0]==1:
                if other[-1]%2==1:
                    ans-=vol(sec)
                else:
                    ans+=vol(sec)
            add.append(sec+[other[-1]+1])
    total.append(cube+[1])
    total+=add
    if cube[0]==1:
        ans+=vol(cube)
print(ans)
