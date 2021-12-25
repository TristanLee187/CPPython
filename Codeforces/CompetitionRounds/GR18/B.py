from sys import stdin
from collections import defaultdict
from itertools import accumulate

input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

places=defaultdict()
bins=[bin(i)[2:].zfill(18) for i in range(2*10**5+2)]
for i in range(18):
    places[i] = list(accumulate([int(bins[j][i]=='0') for j in range(2*10**5+2)]))
for _ in range(rn()):
    l,r=rns()
    ans=float('inf')
    for i in range(18):
        ans=min(ans, places[i][r]-places[i][l-1])
    print(ans)