t = int(input())
for _ in range(t):
    from math import ceil
    n,k = map(int,input().split())
    l=[]
    for i in range(n):
        a=list(map(int,input().split()))
        l.append(a)
    l.sort()
    ans=0
    r=0
    for i in l:
        if i[0]>r:
            r=i[0]
        if i[1]>r:
            a=ceil((i[1]-r)/k)
            ans+=a
            r+=a*k

    print('Case #' + str(_ + 1) + ': ' + str(ans))

