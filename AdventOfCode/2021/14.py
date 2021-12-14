from collections import defaultdict, Counter
prob="input"

file=open(prob+".txt")

rn=lambda:int(line)
rns=lambda:map(int,line.split())
rl=lambda:list(map(int,line.split()))
rs=lambda:line.strip()

ans=0
length=100
lines = file.readlines()
file.close()
d=defaultdict(int)
c=Counter(lines[0].strip())
for i in range(len(lines[0].strip())-1):
    d[lines[0][i:i+2]]+=1

for i in range(40):
    new_d=d.copy()
    for j in range(2,length+2):
        line=lines[j]
        pair,insert = rs().split(' -> ')
        if pair in d:
            c[insert]+=d[pair]
            new_d[pair]-=d[pair]
            new_d[pair[0]+insert]+=d[pair]
            new_d[insert+pair[1]]+=d[pair]
    d=new_d.copy()

ans=max(c.values())-min(c.values())
print(ans)
# print(c)
# print(d)
