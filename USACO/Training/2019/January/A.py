prob="planting"

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
a=[]
for i in range(n-1):
    a.append(rl())
#
file.close()

#CODE
ans=n
d={}
for i in a:
    if i[0] in d:
        d[i[0]].add(i[1])
    else:
        d[i[0]]=set()
        d[i[0]].add(i[1])
    if i[1] in d:
        d[i[1]].add(i[0])
    else:
        d[i[1]]=set()
        d[i[1]].add(i[0])
m=0
for i in d:
    m=max(m,len(d[i]))
ans=m+1
#

file=open(prob+".out","w")
file.write(str(ans))
file.close()
