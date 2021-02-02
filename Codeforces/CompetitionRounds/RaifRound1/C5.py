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
    b=0
    for i in s[::-1]:
        if i=='B':
            b+=1
        else:
            if b==0:
                ans+=1
            else:
                b-=1
    if b>0:
        ans+=(-b)%2
    print(ans)
