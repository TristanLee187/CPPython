t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))

    d={}
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    
    if len(d)==1:
        print(0)
    else:
        l.clear()
        for i in d:
            l.append(d[i])
        l=sorted(l)[::-1]
        if l[0]==2:
            print(n-1-l.count(2))
        else:
            print(int((n-l[0])/(l[0]-1)))
                
