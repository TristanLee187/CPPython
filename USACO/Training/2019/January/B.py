prob="perimeter"

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
grid=[]
for i in range(n):
    grid.append(rs())
#
file.close()

#CODE
ans=''
#

file=open(prob+".out","w")
file.write(str(ans))
file.close()