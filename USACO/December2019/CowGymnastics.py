file = open("gymnastics.in")
l = file.readline().split(' ')
a = int(l[0])
n = int(l[1])
comps = file.readlines()
for i in range(a):
    comps[i] = comps[i].split(' ')
    comps[i] = list(map(int, comps[i]))

file.close()

newl = []
for i in range(n):
    newl.append([])
    for j in range(n):
        newl[i].append(0)

ans=0

for i in range(a):
    for j in range(n):
        for k in range(j+1,n):
            newl[comps[i][j]-1][comps[i][k]-1]+=1


for i in newl:
    for j in i:
        if j==a:
            ans+=1

file = open("gymnastics.out", "w")
file.write(str(ans))
file.close()


