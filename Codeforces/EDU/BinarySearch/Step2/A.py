w,h,n=map(int,input().split())
def f(x,a,b,n):
    return (x//a) * (x//b) >= n
l=1
r=n*max(w,h)
while l<r-1:
    mid=(l+r)//2
    if f(mid,w,h,n):
        r=mid
    else:
        l=mid
print(r)
