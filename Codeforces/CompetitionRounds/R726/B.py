from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from itertools import combinations_with_replacement

for _ in range(rn()):
    n,m,i,j=rns()
    corners=[(1,1),(1,m),(n,1),(n,m)]
    poss=combinations_with_replacement(corners,2)
    ma=-1
    ans=0
    for p in poss:
        dist=abs(i-p[0][0])+abs(j-p[0][1])
        dist+=abs(p[1][0]-p[0][0])+abs(p[1][1]-p[0][1])
        dist+=abs(i - p[1][0]) + abs(j - p[1][1])
        if dist>ma:
            ma=dist
            ans=p
    print(ans[0][0],ans[0][1],ans[1][0],ans[1][1])
