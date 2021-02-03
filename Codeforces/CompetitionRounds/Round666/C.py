n=int(input())
l=list(map(int,input().split()))
if n==1:
    print(1,1)
    print(1)
    print(1,1)
    print(1)
    print(1,1)
    print(l[0]+2)
elif n%2==0:
    print(1,1)
    print(-l[0])
    print(2,n)
    a=[]
    for i in range(1,n):
        if l[i]%2==0:
            a.append(2*n-2)
            l[i]+=2*n-2
            l[i]=-l[i]
        else:
            a.append(n-1)
            l[i]+=n-1
            l[i]=-l[i]
    print(' '.join(list(map(str,a))))
    print(1,n)
    print(' '.join(list(map(str,[0]+l[1:]))))
else:
    print(1,3)
    a=[]
    for i in range(3):
        if l[i]%2==0:
            a.append('6')
            l[i]+=6
        else:
            a.append('3')
            l[i]+=3
    l[0]=-l[0]
    l[1]=-l[1]
    print(' '.join(a))
    print(3,n)
    a=[]
    for i in range(2,n):
        if l[i]%2==0:
            a.append(str(2*(n-2)))
            l[i]+=2*(n-2)
            l[i] = -l[i]
        else:
            a.append(str(n-2))
            l[i]+=n-2
            l[i] = -l[i]
    print(' '.join(a))
    print(1,n)
    print(' '.join(list(map(str,l))))



