from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import Counter

for _ in range(rn()):
    s=rs()
    c=Counter(s)
    ans=0
    for i in c:
        if c[i]>=2:
            ans+=1

    ans += (len(c)-ans)//2
    print(ans)
