rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rns = lambda: map(int, input().split())
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    l=rl()
    l.sort()
    d={}
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            a = l[i] + l[j]
            if a in d:
                d[a]+=1
            else:
                d[a]=1
    d={i:d[i] for i in sorted(d.keys())}
    print(d)
