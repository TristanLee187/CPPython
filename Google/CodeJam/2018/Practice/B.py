rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
mod = lambda x: x % (10 ** 9 + 7)

for _ in range(rn()):
    ans = []
    n=rn()
    p=rl()
    if n==2:
        ans = ' '.join(p[0]*['AB'])
    else:
        while sum(p)>2:
            i=p.index(max(p))
            p[i]-=1
            ans.append(chr(i+65))
        chars=[i+65 for i in range(n) if p[i]==1]
        ans.append(chr(chars[0])+chr(chars[1]))
        ans=' '.join(ans)
    print('Case #' + str(_ + 1) + ': ' + str(ans))