rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
pl = lambda l: print(' '.join(list(map(str, l))))

for _ in range(rn()):
    ans = 0
    s=rs()
    l=len(s)*[0]
    acc=0
    for i in range(len(s)-5,-1,-1):
        if s[i:i+5]=='START':
            acc+=1
        l[i]=acc
    for i in range(len(s)-4):
        if s[i:i+4]=='KICK':
            ans+=l[i]

    print('Case #' + str(_ + 1) + ': ' + str(ans))
