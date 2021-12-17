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
    s=rs()
    t=rs()
    c=Counter(s)
    ans=''
    if 'a' in c and 'b' in c and 'c' in c:
        if t=='abc':
            t='acb'
        else:
            t='abc'
        for ch in t:
            ans+=c[ch]*ch
            del c[ch]
    for ch in sorted(c.keys()):
        ans+=c[ch]*ch
    print(ans)