from sys import stdin
from math import gcd

input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

def lcm(a,b):
    return a*b//gcd(a,b)
for _ in range(rn()):
    n=rn()
    ans=0
    d=1
    i=1
    while True:
        d=lcm(d, i)
        if d>n:
            break
        ans+=n//d
        i+=1
    ans = (ans+n)%mod
    print(ans)