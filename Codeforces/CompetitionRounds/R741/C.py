from sys import stdin
from math import ceil
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    s=rs()
    if '0' not in s:
        print(1,n-n%2,1,n//2)
    else:
        i=s.index('0')
        if i < ceil(n / 2):
            print(i + 1, n, i + 2, n)
        else:
            print(1, i+1, 1, i)
