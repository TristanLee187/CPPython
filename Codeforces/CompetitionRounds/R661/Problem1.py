t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l=sorted(l)
    ans=True
    for i in range(n-1):
        if l[i+1]-l[i]>1:
            ans=False
            break
    if ans:
        print('YES')
    else:
        print('NO')
