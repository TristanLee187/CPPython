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
    n=rn()
    a=rl()
    a.sort(key=lambda x:x%2)
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            ans += int(gcd(a[i],2*a[j])>1)
    print(ans)