rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    l=rl()
    a=[0]+sorted([i for i in l if i%2==0])
    b=[0]+sorted([i for i in l if i%2==1])
    A=0
    B=0
    for c in range(n):
        if c%2==0:
            if a[-1]>b[-1]:
                A+=a.pop()
            else:
                b.pop()
        else:
            if a[-1]<b[-1]:
                B+=b.pop()
            else:
                a.pop()
    if A>B:
        print('Alice')
    elif A==B:
        print('Tie')
    else:
        print('Bob')

