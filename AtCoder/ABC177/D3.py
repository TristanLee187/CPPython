n,q=map(int,input().split())
track=(n+1)*[0]
l=[]
for i in range(q):
    j, k = map(int, input().split())
    j, k = min(j, k), max(j, k)
    l.append([j,k])
l.sort()

for i in l:
    j=i[0]
    k=i[1]
    if track[j]==0 and track[k]==0:
        track[j]={k:1}
        track[k]=-j
    elif type(track[j]) is int and track[j]<0:
        track[-track[j]][k]=1
        track[k]=track[j]
    elif type(track[j]) is int and track[k]<0:
        track[-track[k]][j]=1
        track[j]=track[k]
    elif type(track[k]) is dict:
        for f in k:
            track[j][f]=1
    else:
        track[j][k]=1
ans=1
for i in track:
    if type(i) is dict:
        ans=max(ans,1+len(i))
print(ans)