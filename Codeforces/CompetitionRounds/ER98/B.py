rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    l=rl()
    l.sort()
    a=[l[-1]-i for i in l]
    ans=sum(a)-a[0]
    if n==2:
        print(0)
    elif l[0]<=ans:
        print(ans-l[0])
    else:
        l[0]-=ans
        m=l[0]%(n-1)
        print((n-1-m)%(n-1))