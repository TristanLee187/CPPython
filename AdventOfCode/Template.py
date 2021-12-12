prob="input"

file=open(prob+".txt")

rn=lambda:int(line)
rns=lambda:map(int,line.split())
rl=lambda:list(map(int,line.split()))
rs=lambda:line.strip()

ans=0
lines = file.readlines()
n=len(lines)
file.close()

for line in lines:
    # io
    pass

print(ans)
