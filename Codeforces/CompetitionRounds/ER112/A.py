from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from math import ceil

for _ in range(rn()):
    n=rn()
    if n<7:
        print(15)
    elif n<9:
        print(20)
    elif n<11:
        print(25)
    else:
        ans = 2*(n-(n&1)) + n//2
        ans += 5*(n&1)
        print(int(ans))


