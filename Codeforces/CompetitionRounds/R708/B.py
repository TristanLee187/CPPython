rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import Counter
for _ in range(rn()):
    n,m=rns()
    a=rl()
    b=[a[i]%m for i in range(n)]
    c=Counter(b)
    s=set(b)
    ans=0
    for num in s:
        comp = (m-num)%m
        if comp in c:
            add=abs(c[num]-c[comp])+1
            if c[num]!=c[comp]:
                add-=1
            ans+=add
            del c[num]
            del c[comp]
        else:
            ans+=c[num]
            del c[num]
    print(ans)