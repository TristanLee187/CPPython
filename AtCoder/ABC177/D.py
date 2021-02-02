n,q=map(int,input().split())
d={}
l=[]
for i in range(q):
    j,k=map(int,input().split())
    j,k=min(j,k),max(j,k)
    l.append([j,k])
l.sort()
newl=[l[0]]
for i in range(1,len(l)):
    if l[i]!=newl[-1]:
        newl.append(l[i])

for i in newl:
    j=i[0]
    k=i[1]
    if j in d:
        d[j][k]=1
    else:
        flag=False
        for g in d:
            if j in d[g]:
                d[g][k]=1
                flag=True
        if not flag:
            d[j]={k:1}
print(d)
ans=0
for i in d:
    ans=max(ans,1+len(d[i]))
print(ans)


