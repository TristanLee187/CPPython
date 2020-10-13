n=int(input())
l=list(map(int,input().split()))
ans=0
d={}
for i in range(0,n,2):
    if l[i] in d:
        d[l[i]]+=1
    else:
        d[l[i]]=1
ans+=n//2-max(d.values())
d={}
for i in range(1,n,2):
    if l[i] in d:
        d[l[i]]+=1
    else:
        d[l[i]]=1
ans+=n//2-max(d.values())
print(ans)
