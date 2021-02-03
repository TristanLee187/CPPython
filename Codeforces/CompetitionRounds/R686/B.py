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
    for i in l:
        a[i]+=1
    ans=-1
    for i in range(len(a)):
        if a[i]==1:
            ans=l.index(i)+1
            break
    print(ans)