from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from math import gcd
from collections import defaultdict

for _ in range(rn()):
    n=rn()
    s=rs()
    d=0
    k=0
    ratios=defaultdict(int)
    ans=[]
    for i in range(n):
        if s[i]=='D':
            d+=1
        else:
            k+=1
        if k==0:
            ans.append(d)
        elif d==0:
            ans.append(k)
        else:
            g=gcd(k,d)
            ratio = (k//g, d//g)
            ans.append(ratios[ratio]+1)
            ratios[ratio]+=1
    print(*ans)