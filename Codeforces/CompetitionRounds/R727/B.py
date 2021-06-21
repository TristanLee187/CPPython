from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import defaultdict


n,q=rns()
s=rs()
pre=[]
d=defaultdict(int)
for char in s:
    d[char]+=1
    pre.append(d.copy())
pre.append(defaultdict(int))
for i in range(q):
    l,r=rns()
    l-=1
    r-=1
    ans=0
    for j in range(1,27):
        char=chr(96+j)
        ans+=j*(pre[r][char]-pre[l-1][char])
    print(ans)
