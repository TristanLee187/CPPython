rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import Counter
for _ in range(rn()):
    n =rn()
    a=rl()
    c=Counter(a)
    b=sorted(list(set(a)))
    ans=[]
    for i in b:
        ans.append(i)
        c[i]-=1
    for i in c:
        ans+=c[i]*[i]
    print(*ans)