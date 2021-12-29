from sys import stdin
from collections import Counter
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
    a=rl()
    c=Counter([abs(i) for i in a])
    ans=0
    for num in c:
        if c[num]==1 or num==0:
            ans+=1
        else:
            ans+=2
    print(ans)