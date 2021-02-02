prob="gymnastics"

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
k,n=rns()
l=[]
for i in range(k):
    l.append(rl())
#
file.close()

#
#CODE
ans=0
m=[]
for i in range(n+1):
    m.append((n+1)*[0])

for i in range(k):
    for j in range(n):
        for c in range(j+1,n):
            m[l[i][j]][l[i][c]]+=1
for i in m:
    for j in i:
        if j==k:
            ans+=1
#
file=open(prob+".out","w")
file.write(str(ans))
file.close()