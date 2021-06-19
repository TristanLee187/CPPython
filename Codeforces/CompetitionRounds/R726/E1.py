from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from math import ceil

n,k=rns()
s=rs()
ans=''
for i in range(1,n+1):
    pre=s[:i]
    pans=(ceil(k/len(pre))*pre)[:k]
    if ans=='':
        ans=pans
    else:
        ans=min(ans,pans)
print(ans)