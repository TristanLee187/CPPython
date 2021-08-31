prob="PROB_NAME"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

ans=''
#
#Read input
#
file.close()

file=open(prob+".txt","w")
file.write(str(ans))
file.close()
