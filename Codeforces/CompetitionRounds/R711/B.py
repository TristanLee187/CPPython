rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from collections import Counter

for _ in range(rn()):
    n,W=rns()
    w=rl()
    c=Counter(w)
    grid = n*[0]
    full=0
    for num in sorted(c.keys(), reverse=True):
        j=full
        k=0
        while k<c[num]:
            if grid[j]+num<=W:
                grid[j]+=num
                if grid[j]==W:
                    full+=1
                    j+=1
                k+=1
            else:
                j+=1

    ans=len([i for i in grid if i>0])
    print(ans)