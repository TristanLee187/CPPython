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
    ans=max(0,n-2)
    for i in range(n):
        for j in range(i+1,n):
            pans=0
            for k in range(n):
                if k not in [i,j] and (i-k)*(a[j]-a[i])!=(j-i)*(a[i]-a[k]):
                    pans+=1
            ans=min(ans,pans)
    print(ans)