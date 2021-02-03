rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
pl = lambda l: print(' '.join(list(map(str, l))))
for _ in range(rn()):
    n=rn()
    l=rl()
    l.sort()
    ans=False
    for i in range(1,n):
        if l[i]==l[i-1]:
            ans=True
            break
    yn(ans)
