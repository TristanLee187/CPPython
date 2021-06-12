from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import Counter
from math import gcd

s=rs().strip()
c=Counter(s)
g=gcd(*[c[i] for i in c])
ans=''
if len(c)==1:
    ans=s
elif g>1:
    name=''
    for i in c:
        name+=i*(c[i]//g)
    ans=g*name
else:
    ans='IMPOSSIBLE'
print(ans)