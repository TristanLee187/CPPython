from sys import stdin
from bisect import bisect_left
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n=rn()
a=rl()
a.sort()
s=sum(a)
m=rn()
for _ in range(m):
    de,atk=rns()
    j=bisect_left(a,de)
    if j==n:
        j-=1
    ans=[]
    if j>0:
        ans.append(max(0,de-a[j-1])+max(0,atk-(s-a[j-1])))
    ans.append(max(0,de - a[j]) + max(0, atk - (s - a[j])))
    print(min(ans))