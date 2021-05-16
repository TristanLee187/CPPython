from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from math import gcd

for _ in range(rn()):
    k=rn()
    d=gcd(k,100)
    print(100//d)