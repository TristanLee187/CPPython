rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    l=rl()
    acc=n*[0]
    acc[-1]=l[-1]
    for i in range(n-2,-1,-1):
        if i+l[i]<n:
            acc[i]+=acc[i+l[i]]+l[i]
        else:
            acc[i]=l[i]
    print(max(acc))