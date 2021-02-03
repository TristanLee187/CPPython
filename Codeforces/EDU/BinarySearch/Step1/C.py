n,k=map(int,input().split())
l=list(map(int,input().split()))
q=list(map(int,input().split()))

def searchright(x,a):
    l=0
    r=len(a)-1
    while l<r:
        mid=(l+r)//2
        if a[mid]>=x:
            r=mid
        else:
            l=mid+1
    if a[l]>=x:
        return l+1
    return l+2

for i in q:
    print(searchright(i,l))