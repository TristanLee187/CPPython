file=open("input.txt")

rn=lambda:int(file.readline())
rns=lambda:map(int,file.readline().split())
rl=lambda:list(map(int,file.readline().split()))
rs=lambda:file.readline().strip()

a=[0]
for i in range(2237):
    n=rs()
    if n.isnumeric():
        a[-1]+=int(n)
    else:
        a.append(0)
file.close()
a.sort(reverse=True)
ans=sum(a[:3])
print(ans)
