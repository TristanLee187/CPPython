rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))
def d(a):
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

from math import ceil

for _ in range(rn()):
    n,x=rns()
    l=rl()
    ans=[0,0]
    for i in range(n):
        ans[0]+=ceil(l[i]/x)
    ans[-1]=ceil(sum(l)/x)
    print(*sorted(ans))