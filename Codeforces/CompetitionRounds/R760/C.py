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
    scrap=rl()
    a=[]
    b=[]
    for i in range(n):
        if i%2==0:
            a.append(scrap[i])
        else:
            b.append(scrap[i])
    def comp(arr):
        ans=arr[0]
        for i in range(1,len(arr)):
            ans=gcd(ans, arr[i])
        return ans
    agcd=comp(a)
    bgcd=comp(b)
    arems=[i%bgcd for i in a]
    brems=[i%agcd for i in b]
    if 0 not in arems:
        print(bgcd)
    elif 0 not in brems:
        print(agcd)
    else:
        print(0)