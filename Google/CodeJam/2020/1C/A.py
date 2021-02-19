rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
mod = lambda x: x % (10 ** 9 + 7)

for _ in range(rn()):
    inp=input().split()
    x=int(inp[0])
    y=int(inp[1])
    s=inp[2]
    ans='IMPOSSIBLE'
    for i in range(len(s)):
        if s[i]=='N':
            y+=1
        elif s[i]=='S':
            y-=1
        elif s[i]=='W':
            x-=1
        else:
            x+=1
        if i+1>=abs(x)+abs(y):
            ans=str(i+1)
            break
    print('Case #' + str(_ + 1) + ': ' + ans)