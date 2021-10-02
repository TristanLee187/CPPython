from sys import stdin
from heapq import *
from collections import defaultdict
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=[-num for num in rl()]
    # n=2*10**5
    # a=list(range(2*10**5))
    d=defaultdict(list)
    for i in range(n):
        d[a[i]].append(i)
    heapify(a)
    c=0
    # print(d)
    ans=[]
    while True:
        x=heappop(a)
        y=heappop(a)
        if 0 in [x,y]:
            break
        c+=1
        p0=d[x].pop()
        p1=d[y].pop()
        ans.append((p0+1,p1+1))
        x+=1
        y+=1
        d[x].append(p0)
        d[y].append(p1)
        heappush(a,x)
        heappush(a,y)
    print(c)
    for row in ans:
        print(*row)