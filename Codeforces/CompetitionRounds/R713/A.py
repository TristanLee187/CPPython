rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import Counter
for _ in range(rn()):
    n=rn()
    a=rl()
    c=Counter(a)
    for i in range(n):
        if c[a[i]]==1:
            print(i+1)