rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')

for _ in range(rn()):
    s=rs()
    ans=0
    b=0
    for i in s:
        if i=='(':
            b+=1
        elif i==')':
            if b>0:
                ans+=1
                b-=1
    b = 0
    for i in s:
        if i == '[':
            b += 1
        elif i == ']':
            if b > 0:
                ans += 1
                b -= 1
    print(ans)