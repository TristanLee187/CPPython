prob="input"

file=open(prob+".txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()


#Read input

d=0
h=0
aim=0
for i in range(1000):
    a,b=rs().split()
    b=int(b)
    if a[0]=='f':
        h+=b
        d+=b*aim
    elif a[0]=='d':
        aim+=b
    else:
        aim-=b

file.close()

ans=d*h
print(ans)
