from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import defaultdict
from itertools import accumulate
for _ in range(rn()):
    n=rn()
    u=rl()
    s=rl()
    d=defaultdict(list)
    for i in range(n):
        d[u[i]].append(s[i])
    for i in d:
        d[i].sort(reverse=True)
    for i in d:
        pre=list(accumulate(d[i]))
        d[i]=pre
    ans=[]
    for i in range(1,n+1):
        ans.append(0)
        dels=[]
        for j in d:
            pre = d[j]
            if len(pre)<i:
                # d.pop(j)
                dels.append(j)
            else:
                ans[-1]+=pre[len(pre) - len(pre)%i - 1]
        for j in dels:
            d.pop(j)
    print(*ans)