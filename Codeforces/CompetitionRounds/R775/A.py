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
    r=0
    while r<n-1 and a[r]==1 and a[r+1]==1:
        r+=1
    l=n-1
    while l>0 and a[l]==1 and a[l-1]==1:
        l-=1
    print(max(0,l-r))