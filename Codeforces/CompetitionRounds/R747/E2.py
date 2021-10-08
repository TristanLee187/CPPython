from sys import stdin
from collections import defaultdict
input = stdin.readline
rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input().strip()
YN = lambda x: print('YES') if x else print('NO')
mod = 10 ** 9 + 7

CO = {
    'w':['w','y'],
    'y':['w','y'],
    'r':['r','o'],
    'o':['r','o'],
    'b':['b','g'],
    'g':['b','g']
}

k=rn()
n=rn()
KK=2**k
nodes={}
for _ in range(n):
    v,color = rs().split()
    v=int(v)
    color=color[0]
    nodes[v]=color
con=False
ans=6
p=2*(2**k-2)
affected=defaultdict(set)
for node in nodes:
    parent=node//2
    if parent:
        affected[parent].add(CO[nodes[node]][0])
    children = [2*node,2*node+1]
    for child in children:
        if child < KK:
            affected[child].add(CO[nodes[node]][0])

for node in affected:
    if node in nodes:
        if node==1:
            ans=1
        else:
            p-=1
        if nodes[node] in affected[node]:
            con=True
            break
    else:
        if len(affected[node])==3:
            con=True
            break
        else:
            if node==1:
                ans-=2*len(affected[node])
            elif len(affected[node])==2:
                p-=1

for node in nodes:
    if node not in affected:
        if node==1:
            ans=1
        else:
            p-=2

if con:
    print(0)
else:
    ans *= pow(4, p, mod)
    print(ans % mod)