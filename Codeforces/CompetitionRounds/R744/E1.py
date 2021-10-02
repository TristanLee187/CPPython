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
    n=rn()
    p=rl()
    d=deque()
    for num in p:
        if len(d)==0:
            d.append(num)
        elif num<d[0]:
            d.appendleft(num)
        else:
            d.append(num)
    print(*d)