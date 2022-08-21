from sys import stdin
from math import ceil
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    ans=1
    n=rn()
    n-=1
    ans+=n//5
    print('Case #' + str(_+1)+': ' + str(ans))