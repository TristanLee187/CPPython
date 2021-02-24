rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

import bisect

n,m=rns()
s=rs()
t=rs()
d={}
for i in range(n):
    if s[i] not in d:
        d[s[i]]=[]
    d[s[i]].append(i)
lbounds=[]
for i in range(m):
    lo=0
    if i==0:
        lo=d[t[i]][0]
    else:
        j=bisect.bisect_right(d[t[i]],lbounds[-1])
        lo=d[t[i]][j]
    lbounds.append(lo)
hbounds=[]
for i in range(m-1,-1,-1):
    hi=0
    if i==m-1:
        hi=d[t[i]][-1]
    else:
        j = bisect.bisect_left(d[t[i]], hbounds[-1])
        hi = d[t[i]][j-1]
    hbounds.append(hi)
hbounds.reverse()

ans=0
for i in range(m-1):
    lo=0
    hi=0
    if i==0:
        lo=d[t[i]][0]
    else:
        j=bisect.bisect_right(d[t[i]],lbounds[i-1])
        lo=d[t[i]][j]
    if i+1==m-1:
        hi=d[t[i+1]][-1]
    else:
        j = bisect.bisect_left(d[t[i+1]], hbounds[i + 2])
        hi = d[t[i+1]][j-1]
    ans=max(ans,hi-lo)
print(ans)