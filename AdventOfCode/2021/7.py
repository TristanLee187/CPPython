prob="input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

a=rs().split(',')
a=list(map(int,a))
a.sort()
print(a[-1])
n=len(a)

avg = int(sum(a)/len(a))
sans=0
for num in a:
    sans+=abs(num-avg)*(abs(num-avg)+1)//2

tans=0
avg+=1
for num in a:
    tans+=abs(num-avg)*(abs(num-avg)+1)//2
file.close()

print(min(sans,tans))
