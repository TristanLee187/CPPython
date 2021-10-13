from sys import stdin
from collections import defaultdict
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rs()
    ends=['25','50','75','00']
    ans=float('inf')
    d=defaultdict(list)
    for i in range(len(n)):
        d[n[i]].append(i)
    # print(d)
    for end in ends:
        if end=='00' and len(d['0'])>=2:
            pans=len(n) - min(d['0'][-1],d['0'][-2]) - 2
            ans=min(ans,pans)
        elif len(d[end[0]])>=1 and len(d[end[1]])>=1:
            right=d[end[1]][-1]
            left=len(d[end[0]])-1
            while left>-1 and d[end[0]][left]>right:
                left-=1

            if left>-1 and d[end[0]][left]<right:
                pans = len(n)-d[end[0]][left]-2
                ans=min(ans,pans)

    print(ans)