n,k=map(int,input().split())
l=list(map(int,input().split()))
q=list(map(int,input().split()))

def searchleft(x,a):
    l=0
    r=len(a)-1
    while l<r:
        mid=int((l+r)/2 + 0.5*((l+r)%2==1))
        if a[mid]<=x:
            l=mid
        else:
            r=mid-1
    if a[l]<=x:
        return l+1
    return l

for i in q:
    print(searchleft(i,l))