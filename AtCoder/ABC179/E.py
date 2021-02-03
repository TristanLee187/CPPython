n,x,m=map(int,input().split())
d={}
l=[]
i=x
while i%m not in d:
    a=i%m
    d[a]=1
    l.append(a)
    i=(i*i)%m
ans=0
s=0
j=-1
while l[j]!=i%m:
    s+=l[j]
    j-=1
j+=len(l)
ans+=sum(l[:j])
ans+=(n//(len(l)-j))*s
print(ans)
print(l)
