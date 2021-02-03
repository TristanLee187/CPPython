n,k=map(int,input().split())
l=list(map(int,input().split()))
def search(x,a):
    l=0
    r=len(a)-1
    while l<r:
        mid=(l+r)//2
        if a[mid]==x:
            return True
        if a[mid]<x:
            l=mid+1
        else:
            r=mid-1
    return a[l]==x

q=list(map(int,input().split()))
for i in range(k):
    if search(q[i],l):
        print('YES')
    else:
        print('NO')