t=int(input())
count=0
while count<t:
    count+=1
    l=list(map(int, input().split(' ')))
    n = l[0]
    k = l[1]
    if k>=n:
        print(1)
    else:
        l=[]
        factor = 1
        while factor<=n**0.5:
            if n%factor==0:
                l.append(factor)
            factor+=1
 
        m = list(map(lambda x: n/x, l))
        m = m + l[::-1]
        for i in m:
            if i<=k:
                print(int(n/i))
                break
