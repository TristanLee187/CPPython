t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))

    m=max(l)
    l1=[m-i for i in l]
    m=max(l1)
    l2=[m-i for i in l1]
    if k%2==0:
        print(' '.join(list(map(str,l2))))
    else:
        print(' '.join(list(map(str,l1))))