t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    m=min(l)
    d=[]
    s=[]
    for i in range(len(l)):
        if l[i]%m!=0:
            d.append(l[i])
            if len(s)==0:
                s.append(i)
            else:
                s.append(i-s[-1]-1)
    if not all([d[i]>=d[i-1] for i in range(1,len(d))]):
        print('NO')
    elif len(d)==0:
        print('YES')
    else:
        from bisect import *
        if l[-1]%m==0:
            d.append(10**9+1)
            s.append(len(l) - s[-1]-1)
        ans=True
        for i in range(len(l)):
            if l[i]%m==0:
                j=bisect_left(d,l[i])
                if s[j]==0:
                    ans=False
                    break
                else:
                    s[j]-=1
        if ans:
            print('YES')
        else:
            print('NO')
