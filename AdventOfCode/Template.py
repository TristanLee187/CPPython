prob="input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

ans=0


file.close()

print(ans)