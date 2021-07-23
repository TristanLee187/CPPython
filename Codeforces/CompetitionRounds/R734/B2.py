from sys import stdin

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input().strip()
YN = lambda x: print('YES') if x else print('NO')
mod = 10 ** 9 + 7
from collections import defaultdict

for _ in range(rn()):
    n,k=rns()
    a=rl()
    indeces=defaultdict(list)
    for i in range(n):
        indeces[a[i]].append(i)
    ans=n*[0]

    for i in indeces:
        if len(indeces[i])>=k:
            for j in range(k):
                ans[indeces[i][j]]=j+1
            indeces[i].clear()

    more=0
    for i in indeces:
        if indeces[i]:
            more+=len(indeces[i])

    more=k*(more//k)
    c=0
    for i in indeces:
        if indeces[i]:
            for j in indeces[i]:
                if c==more:
                    break
                ans[j]=(c%k)+1
                c+=1
            if c==more:
                break

    print(*ans)
