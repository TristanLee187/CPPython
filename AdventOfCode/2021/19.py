from collections import defaultdict

file=open("input.txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

scans=defaultdict(list)
lines=file.readlines()
c=0
i=1
ns=5
req=12
while i<len(lines):
    if len(lines[i].strip())!=0:
        if lines[i][:2]=='--':
            c+=1
        else:
            scans[c].append(eval('(' + lines[i]+')'))
    i+=1
file.close()
def perms(index, x,y,z):
    l=[(x, y, z), (y, x, -z), (-y, z, -x), (z, y, -x), (z, x, y), (-z, x, -y), (-y, x, z), (x, -z, y), (-z, -x, y), (x,
        -y, -z), (y, -x, z), (z, -x, -y), (y, -z, -x), (-y, -x, -z), (-x, -y, z), (-z, -y, -x), (-x, z, y), (-x, -z, -y)
        , (x, z, -y), (-x, y, -z), (z, -y, x), (y, z, x), (-y, -z, x), (-z, y, x)]
    return l[index]

def match(p1, p2):
    s1=set(p1)
    for ii in range(len(p1)):
        for jj in range(len(p2)):
            dx= p1[ii][0] - p2[jj][0]
            dy= p1[ii][1] - p2[jj][1]
            dz= p1[ii][2] - p2[jj][2]
            s2=set((x+dx, y+dy,z+dz) for x,y,z in p2)
            if len(s1&s2)>=req:
                return [True, s2, s1&s2]

    return [False]
points=set(scans[0])
seen={0}
i=0
while len(seen)<ns:
    for j in range(ns):
        found=False
        if i!=j and j not in seen:
            for orient in range(24):
                change = [perms(orient, x,y,z) for x,y,z in scans[j]]
                poss=match(scans[i], change)
                if poss[0]:
                    print(i,j)
                    for point in poss[1]:
                        points.add(point)
                    found=True
                    seen.add(j)
                    i=j
                    scans[j]=list(poss[1])
                    break
        if found:
            break
ans=len(points)
print(ans)
