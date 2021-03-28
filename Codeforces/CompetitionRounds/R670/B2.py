for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    ans=1

    for i in range(n-5,n):
        ans*=l[i]
    for i in range(1,6):
        t=1
        for j in range(i):
            t*=l[j]
        for j in range(5-i):
            t*=l[::-1][j]
        ans=max(ans,int(t))
    print(ans)