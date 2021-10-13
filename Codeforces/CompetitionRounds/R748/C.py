from sys import stdin
from collections import deque
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,k=rns()
    x=rl()
    x.sort()
    x = deque(x)
    ans=0
    time=0
    while x:
        need=n-x.pop()
        time+=need
        ans+=1
        while x and x[0]<=time:
            x.popleft()
    print(ans)