from sys import stdin
from collections import Counter
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    p=[tuple(rns()) for _ in range(n)]
    typs=Counter([pair[0] for pair in p])
    diffs=Counter([pair[1] for pair in p])
    typ_sum=0
    diff_sum=0
    for num in typs:
        typ_sum += typs[num]*(n-typs[num])
    for num in diffs:
        diff_sum += diffs[num]*(n-diffs[num])

    # print(typ_sum,diff_sum)
    ans=0
    for typ in typs:
        typ_ways = typs[typ]*(typ_sum-(2*typs[typ]*(n-typs[typ])))//2
        ans+=typ_ways
    for diff in diffs:
        diff_ways = diffs[diff]*(diff_sum-(2*diffs[diff]*(n-diffs[diff])))//2
        ans+=diff_ways

    print(ans)