rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

import bisect

n=rn()
l=rl()
b=sorted(list(set(l)))
print(b)
a=[]
for i in range(n):
    a.append(bisect.bisect_left(b,l[i]))
m=min(a)
if m<0:
    for i in range(n):
        a[i]+=-m
d={}
for i in range(n):
    if a[i] in d:
        d[a[i]].append(i)
    else:
        d[a[i]]=[i]
ans=0
for i in range(n):
    if a[i]-1 in d:
        j=bisect.bisect_right(d[a[i]-1],i)
        if j==len(d[a[i]-1]) or d[a[i]-1][j]<i:
            ans = max(ans, (n - i) * l[i])
        else:
            ans=max(ans,((d[a[i]-1][j]-i)*l[i]))
    else:
        ans=max(ans,(n-i)*l[i])
print(a)
print(l)
print(d)
print(ans)
l=l[::-1]
a=a[::-1]
for i in d:
    for j in range(len(d[i])):
        d[i][j]=n-d[i][j]-1
    d[i]=d[i][::-1]
for i in range(n):
    if a[i]-1 in d:
        j=bisect.bisect_right(d[a[i]-1],i)
        if j==len(d[a[i]-1]) or d[a[i]-1][j]<i:
            ans = max(ans, (n - i) * l[i])
        else:
            ans=max(ans,((d[a[i]-1][j]-i)*l[i]))
    else:
        ans=max(ans,(n-i)*l[i])
print(a)
print(l)
print(d)
print(ans)