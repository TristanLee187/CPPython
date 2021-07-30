from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from itertools import permutations
from math import ceil

n,m=rns()
s=rs()
ls=[]
for perm in permutations('abc'):
    st=''
    for i in perm:
        st+=i
    comp=int(ceil(n/3))*st
    add=[]
    for i in range(n):
        if i==0:
            if s[i]!=comp[i]:
                add.append(1)
            else:
                add.append(0)
        else:
            if s[i]!=comp[i]:
                add.append(1+add[-1])
            else:
                add.append(add[-1])
    ls.append(add)
for _ in range(m):
    l,r=rns()
    ans=float('inf')
    for test in ls:
        ans=min(ans, test[r-1]-test[l-2] if l>1 else test[r-1])
    print(ans)