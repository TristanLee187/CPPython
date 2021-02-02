rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
pl = lambda l: print(' '.join(list(map(str, l))))

for _ in range(rn()):
    n=rn()
    s=rs()
    ans=0
    modes=set(s)
    circle=False
    if len(modes)==1 or (len(modes)==2 and '-' in modes):
        circle=True
    if circle:
        ans=n
    else:
        for i in range(n):
            if s[i]=='-' or s[(i+1)%n]=='-':
                ans+=1
    print(ans)

