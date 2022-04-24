from sys import stdin
from collections import deque
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    ans=0
    n=rn()
    a=rl()
    d=deque(a)
    last=0
    while len(d)>0:
        if d[0]<d[-1]:
            ans += 1 if d[0]>=last else 0
            last=max(last,d.popleft())
        else:
            ans += 1 if d[-1]>=last else 0
            last=max(last,d.pop())
    print('Case #' + str(_+1)+': ' + str(ans))