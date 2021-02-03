for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    ans=1
    c=5
    p1=0
    p2=n-2
    while c>0:
        if c>1:
            if l[p1]*l[p1+1]>=l[p2]*l[p2+1]:
                ans*=l[p1]*l[p1+1]
                c-=2
                p1+=2
            else:
                ans *= l[p2+1]
                c -= 1
                p2 -= 1
        else:
            ans*=l[p2+1]
            c-=1
    print(ans)






