from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import defaultdict

for _ in range(rn()):
    n,m=rns()
    a=rl()
    d=defaultdict(list)
    people=sorted(a)
    for i in range(m):
        d[people[i]].append(i)
    # print(d)
    taken=[0 for i in range(m)]
    ans=0

    for num in a:
        i=d[num].pop()
        ans+=taken[:i].count(1)
        taken[i]=1

    print(ans)
