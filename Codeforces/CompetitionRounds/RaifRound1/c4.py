rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
pl = lambda l: print(' '.join(list(map(str, l))))

for _ in range(rn()):
    s = rs()
    n = len(s)
    acc = [0]
    last = s[0]
    for c in s:
        if c == last:
            acc[-1] += 1
        else:
            last = c
            acc.append(1)
    i=0
    if s[0]=='B':
        i+=1
    while i<len(acc)-1:
        m=min(acc[i],acc[i-1])
        acc[i]-=m
        acc[i-1]-=m

            





