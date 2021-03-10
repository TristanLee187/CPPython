rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from math import ceil

for _ in range(rn()):
    n,k=rns()
    s=rl()
    m=max(s)
    h=set(s)
    if k==0:
        print(len(h))
    else:
        for i in range(10**9+1):
            if i not in h:
                if i>m:
                    print(len(h)+k)
                elif ceil((i+m)/2) not in h:
                    print(len(h)+1)
                else:
                    print(len(h))
                break