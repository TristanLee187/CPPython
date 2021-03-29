rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from math import gcd

for _ in range(rn()):
    n=rn()
    def f(n):
        ans=0
        for i in str(n):
            ans+=int(i)
        return ans
    while gcd(n,f(n))==1:
        n+=1
    print(n)