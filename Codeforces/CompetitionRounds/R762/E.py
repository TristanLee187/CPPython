from collections import Counter
from sys import stdin
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
    a.sort()
    c=Counter(a)
    ans=[]
    extra=[]
    p=0
    mex=-1
    for i in range(n-1):
        if a[i]<a[i+1]-1:
            mex=a[i]+1
            break
    if mex==-1:
        mex=a[-1]+1

    for i in range(n+1):
        if i<mex:
            ans.append(c[i])
            extra+=[i for j in range(c[i]-1)]
        elif i==mex:
            ans.append(0)
        elif ans[i-1]==-1:
            ans.append(-1)
        elif len(extra)>0:
            ans.append(ans[-1] + i-extra.pop()-1+c[i])
        elif c[i-1]>0:
            ans.append(ans[-1]-c[i-1])
        else:
            ans.append(-1)

    print(*ans)