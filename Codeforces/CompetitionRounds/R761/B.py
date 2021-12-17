from sys import stdin
from math import gcd
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    n=rn()
    if n%2==0:
        print(2,n-3,1)
    else:
        q=1
        k=n//2
        while gcd(k-q, k+q)!=1:
            q+=1
        print(k-q, k+q, 1)