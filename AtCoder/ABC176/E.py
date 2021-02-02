h,w,m=map(int,input().split())
l=[]
for i in range(m):
    l.append(list(map(int,input().split())))
l.sort()
a={}
b={}
for i in l:
    if i[0] in a:
        a[i[0]]+=1
    else:
        a[i[0]]=1
    if i[1] in b:
        b[i[1]]+=1
    else:
        b[i[1]]=1
ma=max(list(b.values()))
c={}
for i in b:
    if b[i]==ma:
        c[i]=1
ans=0
i=0
for j in a:
    e=0
    while i<m and l[i][0]==j:
        if l[i][1] in c:
            e+=1
        i+=1
    tans=a[j]+ma
    if e==len(c):
        tans-=1
    ans=max(ans,tans)
print(ans)