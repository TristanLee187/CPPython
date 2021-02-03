import bisect

t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))

    s=sorted(l)
    a=0
    b=n-1
    ans=0
    for i in s:
        if i==l[a]:
            a+=1
        elif i==l[b]:
            b-=1
        else:
            while l[a]!=i:
                s.pop(bisect.bisect_left(s,l[a]))
                a+=1
                ans=a
            a+=1
    print(ans)
            
            
