t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    a=sorted(l)
    m=min(l)
    ans=True
    for i in range(len(l)):
        if l[i]!=a[i] and l[i]%m!=0:
            ans=False
            break
    if ans:
        print('YES')
    else:
        print('NO')