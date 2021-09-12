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
    n,s=rns()
    if n%2:
        print(s//(ceil(n/2)))
    else:
        print(s // (n // 2 +1))