n=int(input())
l=list(map(int,input().split()))
if n==1:
    print(1,1)
    print(1)
    print(1,1)
    print(1)
    print(1,1)
    print(-(l[0]+2))
else:
    print(1,1)
    a=[]
    print(n-l[0]%n)
    l[0]+=n-l[0]%n
    l[0]*=-1
    for i in range(1,n):
        a.append(l[i]%n*(n-1))
        l[i]+=l[i]%n*(n-1)
        l[i]*=-1
    print(2,n)
    print(' '.join(list(map(str,a))))
    print(1,n)
    print(' '.join(list(map(str,l))))