prob="a_example"

file=open(prob)

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline()
pl=lambda l:file.write(' '.join(list(map(str,l))))

#
#Read input
m,one,two,three=rns()
pizzas={}
for i in range(m):
    s=rs().split()
    pizzas[i]=s[1:]
#
file.close()

#CODE
ans=1
#

file=open(prob+".out","w")
file.write(str(ans)+'\n')
for i in range(ans):
    file.write('2 0 1\n')
file.close()