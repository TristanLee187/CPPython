n,k=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input()))
def f(x,l,k):
    s=sum([i//x for i in l])
    return s>=k

left=0
r=max(l)
while left<r-10**(-6):
    mid=(left+r)/2
    if f(mid,l,k):
        left=mid
    else:
        r=mid

print(r)