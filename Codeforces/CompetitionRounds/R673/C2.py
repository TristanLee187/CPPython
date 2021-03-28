rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')

for _ in range(rn()):
    n=rn()
    l=rl()
    ans=n*[-1]
    a=n*[-1]
    d=n*[0]
    for i in range(n):
        d[l[i]-1]=max(d[l[i]-1],i-a[l[i]-1])
        a[l[i]-1]=i
    for i in range(n):
        d[i]=max(d[i],n-a[i])

    for i in l:
        if ans[d[i-1]-1]==-1:
            ans[d[i - 1] - 1]=i
        else:
            ans[d[i-1]-1]=min(i,ans[d[i-1]-1])

    m=float('inf')
    i=0
    while i<n and ans[i]==-1:
        i+=1
    m=ans[i]
    for j in range(i,n):
        if ans[j]==-1:
            ans[j]=m
        else:
            ans[j]=min(ans[j],m)
        m=min(m,ans[j])
    print(' '.join(list(map(str,ans))))