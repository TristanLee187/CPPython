rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')

for _ in range(rn()):
    q,d=rns()
    l=rl()
    for num in l:
        ans=num>=(d*10)
        if ans:
            print('YES')
        else:
            m=num%d
            for i in range(1,num//d+1):
                if str(d) in str(i*d+m):
                    ans=True
            YN(ans)