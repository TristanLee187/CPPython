# Test set 1

from sys import stdin

input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    ans=0
    d, n, x = rns()
    seeds = [rl() for i in range(n)]
    for i in range(d,0,-1):
        if len(seeds)==0:
            break
        j=0
        max_v=-1
        for k in range(len(seeds)):
            if i+seeds[k][1]<=d and seeds[k][2]>max_v:
                j=k
                max_v=seeds[k][2]
        if max_v!=-1:
            ans+=max_v
            seeds.pop(j)
    print('Case #' + str(_+1)+': ' + str(ans))