# Test set 2

from sys import stdin

input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

def ceildiv(a, b):
    return -(a // -b)

for _ in range(rn()):
    ans=0
    d, n, x = rns()
    seeds = [rl() for i in range(n)]
    seeds.sort(key=lambda x: (x[1], -x[2]))
    print(seeds)

    print('Case #' + str(_+1)+': ' + str(ans))