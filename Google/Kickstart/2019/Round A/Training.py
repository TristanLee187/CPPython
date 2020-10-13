t = int(input())
for _ in range(t):
    n,p=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    diff=[l[i]-l[i-1] for i in range(1,n)]
    curr=0
    s=0
    for i in range(p-1):
        curr+=diff[i]*(i+1)
        s+=diff[i]
    ans=curr
    for i in range(p-1,n-1):
        curr-=s
        curr+=diff[i]*(p-1)
        ans=min(ans,curr)
        s-=diff[i-p+1]
        s+=diff[i]

    print('Case #' + str(_ + 1) + ': ' + str(ans))

