t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    can=min(a)
    orange=min(b)

    ans=0
    for i in range(n):
        thing=max(a[i]-can,b[i]-orange)
        ans+=thing
    print(ans)
