prob="leapfrog_ch_1_input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

#
#Read input
t=rn()
tests=[]
for _ in range(t):
    tests.append(rs())
#
file.close()

#CODE
ans=''
for i in range(t):
    ans+='Case #{}: '.format(i+1)
    s=tests[i]
    a=len(s)-1
    b=s.count('B')
    add = 'Y' if a>b>(a-1)/2 else 'N'
    ans+=add+'\n'
#

file=open(prob+".out","w")
file.write(str(ans))
file.close()
