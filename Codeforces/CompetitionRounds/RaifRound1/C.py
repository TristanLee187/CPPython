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
    acc=[0]
    last=s[0]
    for c in s:
        if c==last:
            acc[-1]+=1
        else:
            last=c
            acc.append(1)
    ans=0
    first=s[0]
    i=0
    if first=='B':
        ans=acc[0]%2
        i=1
    while i<len(acc)-1:
        ans+=abs(acc[i]-acc[i+1])
        i+=2
    if len(acc)==1 and first=='A':
        ans=n
    print(ans)
    print(acc)