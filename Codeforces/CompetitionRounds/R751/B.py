from sys import stdin
from collections import Counter
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rl()
    c=Counter(a)
    ans = [a]
    for __ in range(n):
        b=[c[ans[-1][i]] for i in range(n)]
        ans.append(b)
        c=Counter(b)
    # print(ans)
    q=rn()
    for __ in range(q):
        x,k=rns()
        print(ans[min(k,n)][x-1])
