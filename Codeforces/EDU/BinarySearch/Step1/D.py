n=int(input())
l=list(map(int,input().split()))
l.sort()
k=int(input())

def searchleft(x,a):
    l=0
    r=len(a)-1
    while l<r:
        mid=(l+r)//2
        if a[mid]<=x:
            l=mid
        else:
            r=mid-1
    return l


def searchright(x,a):
    l=0
    r=len(a)-1
    while l<r:
        mid=(l+r)//2
        if a[mid]>=x:
            r=mid
        else:
            l=mid+1
    return l


for i in range(k):
    left,right=map(int,input().split())
    print(searchright(right, l),searchleft(left, l))
    print(searchright(right,l)-searchleft(left,l))