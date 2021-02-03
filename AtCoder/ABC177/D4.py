n,q=map(int,input().split())
l=[]
for i in range(q):
    j, k = map(int, input().split())
    j, k = min(j, k), max(j, k)
    l.append([j,k])
l.sort()
newl=[l[0]]
for i in range(1,len(l)):
    if l[i]!=newl[-1]:
        newl.append(l[i])
