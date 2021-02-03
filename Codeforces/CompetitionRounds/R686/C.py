rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    l=rl()
    a=(max(l)+1)*[0]
    for i in range(len(a)):
        a[i]=[]
    for i in range(n):
        a[l[i]]+=[i]
    ans=float('inf')
    for i in range(len(a)):
        if len(a[i])>0:
            a[i]=[-1]+a[i]
            a[i].append(n)
            tans=0
            for j in range(1,len(a[i])):
                if a[i][j]-a[i][j-1]>1:
                    tans+=1
            ans=min(ans,tans)
    print(ans)
