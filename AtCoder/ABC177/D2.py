n,q=map(int,input().split())
arr=(n+1)*[1]
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
    if arr[j]>0:
        arr[j]+=1
        arr[k]=-j
    elif arr[j]<0:
        arr[-arr[j]]+=1
        arr[k]=arr[j]
print(newl)
print(arr)
print(max(arr))