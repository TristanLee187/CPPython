rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import Counter
from math import ceil

for _ in range(rn()):
    n,m=rns()
    days=[]
    ans=[]
    for i in range(m):
        days.append(rl()[1:])
        ans.append(days[-1][0])
    c=Counter(ans)
    flag=True
    for num in c:
        if c[num]>ceil(m/2):
            for i in range(m):
                if ans[i]==num and len(days[i])>1:
                    ans[i]=days[i][1]
                    c[num]-=1
                    if c[num]==ceil(m/2):
                        break
            if c[num] > ceil(m / 2):
                flag=False
            break
    if flag:
        print('YES')
        print(*ans)
    else:
        print('NO')