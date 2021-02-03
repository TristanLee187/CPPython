prob="moobuzz"

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
#
file.close()

#CODE
ans=(n//8)*15
if n%8==0:
    ans-=1
else:
    add=[0,1,2,4,7,8,11,13,14]
    ans+=add[n%8]
#

file=open(prob+".out","w")
file.write(str(ans))
file.close()