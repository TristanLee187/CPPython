n,x,y=map(int,input().split())
def f(x,a,b,n):
    return x//a+x//b>=n-1

ans=min(x,y)
l=0
r=n*min(x,y)
while l<r-1:
    mid=(l+r)//2
    if f(mid,x,y,n):
        r=mid
    else:
        l=mid
if n==1:
    print(ans)
else:
    print(ans+r)