rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
pl = lambda l: print(' '.join(list(map(str, l))))

for _ in range(rn()):
    s=rs()
    n=len(s)
    ans=0
    bal=0
    acc=0
    for i in range(n):
        if s[i]=='A':
            if bal<0:
                acc+=(-bal)%2
                bal=1
            elif i>0 and s[i-1]=='B':
                ans+=bal
                bal=1
            else:
                bal+=1
        else:
            bal-=1
    if bal<0:
        acc+=-bal
    ans+=acc%2
    if bal>0:
        ans+=bal
    print(ans)
