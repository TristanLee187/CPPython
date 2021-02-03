rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    l=rl()
    d={}
    a=l.count(1)
    b=l.count(2)
    if sum(l)%2==1:
        print('NO')
    else:
        s=sum(l)//2
        if s%2==1:
            YN(a>1)
        else:
            print('YES')