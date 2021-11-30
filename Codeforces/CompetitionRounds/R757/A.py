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
    n,l,r,k=rns()
    a=rl()
    a=sorted([i for i in a if l<=i<=r])
    ans=0
    curr=0
    for i in range(len(a)):
        if curr+a[i]>k:
            break
        curr+=a[i]
        ans+=1
    print(ans)