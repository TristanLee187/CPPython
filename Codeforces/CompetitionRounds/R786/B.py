from sys import stdin
from collections import defaultdict
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

d=defaultdict(int)
for i in range(26):
    for j in range(26):
        if i!=j:
            d[chr(97+i) + chr(97+j)] = len(d)+1

for _ in range(rn()):
    s=rs()
    print(d[s])