from sys import stdin

input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input().strip()
YN = lambda x: print('YES') if x else print('NO')
mod = 10 ** 9 + 7
from collections import defaultdict

n,m=rns()
less=defaultdict(int)
more=defaultdict(int)

for _ in range(m):
    a,b=rns()
    if b>a:
        more[a]+=1
        less[b]+=1
    else:
        less[a]+=1
        more[b]+=1

alive=(n+1)*[1]
for i in range(1,n+1):
    if more[i]:
        alive[i]=0

curr = -1
for i in alive:
    curr+=i

for _ in range(rn()):
    query=rl()
    if query[0]==1:
        a,b=sorted(query[1:])
        more[a]+=1
        less[b]+=1
        if alive[a]:
            alive[a] = 0
            curr -= 1
    elif query[0]==2:
        a, b = sorted(query[1:])
        more[a] -= 1
        less[b] -= 1
        if alive[a]==0 and more[a]==0:
            alive[a]=1
            curr+=1
    else:
        print(curr)

