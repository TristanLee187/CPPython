"""
ID: tristan16
LANG: PYTHON3
PROB: skidesign
"""

prob="skidesign"

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
l=[]
for i in range(n):
    l.append(rn())
#
file.close()

#CODE
l.sort()
ans=float('inf')
for i in l:
    tans=0
    for j in l:
        if j<i:
            tans+=(i-j)**2
        elif j-i>17:
            tans+=(j-i-17)**2
    ans=min(ans,tans)
l=l[::-1]
for i in l:
    tans=0
    for j in l:
        if j>i:
            tans+=(i-j)**2
        elif i-j>17:
            tans+=(i-j-17)**2
    ans=min(ans,tans)
#

file=open(prob+".out","w")
file.write(str(ans)+'\n')
file.close()