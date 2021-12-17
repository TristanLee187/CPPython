file=open("input.txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()


file.close()
xrange = (29, 73)
yrange = (-248, -194)
c=0
for i in range(-10**3, 10**3):
    for j in range(-10**3, 10**3):
        dx, dy=i,j
        x,y=0,0
        while x<xrange[0] or y>yrange[1]:
            if y<yrange[0]:
                break
            x+=dx
            y+=dy
            dx=max(dx-1, 0)
            dy-=1
        if xrange[0]<=x<=xrange[1] and yrange[0]<=y<=yrange[1]:
            c+=1
print(c)
