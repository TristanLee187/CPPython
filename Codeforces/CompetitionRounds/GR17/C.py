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
    a=[list(rns()) for i in range(n)]
    def f(x):
        b,c=x-1,0
        d=0
        for i in range(n):
            if a[i][0]>=b and a[i][1]>=c:
                b-=1
                c+=1
                d+=1
                if d==x:
                    return True
        return False
    lo=1
    hi=n
    ans=1
    while lo<=hi:
        mid=(lo+hi)//2
        if f(mid):
            ans=max(ans,mid)
            lo=mid+1
        else:
            hi=mid-1
    print(ans)
