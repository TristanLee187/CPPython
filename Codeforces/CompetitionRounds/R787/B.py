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
    ans=0
    for i in range(n-1,0,-1):
        if a[i]==0:
            ans=-1
            break
        else:
            while a[i-1]>=a[i]:
                a[i-1]//=2
                ans+=1
    print(ans)
