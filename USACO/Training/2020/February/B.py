prob="triangles"

file=open(prob+".in")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

#
#Read input
n=rn()
p=[]
for i in range(n):
    p.append(rl())
#
file.close()

#CODE
ans=0
p.sort()
xp={}
for po in p:
    if po[0] in xp:
        xp[po[0]].append(po[1])
    else:
        xp[po[0]]=[po[1]]

for po in xp:
    diff=[xp[po][0]]
    for i in xp[po][1:]:
        diff.append(i-diff[-1])
    
yp={}
for po in p:
    if po[1] in yp:
        yp[po[1]].append(po[0])
    else:
        yp[po[1]]=[po[0]]


#

file=open(prob+".out","w")
file.write(str(ans))
file.close()