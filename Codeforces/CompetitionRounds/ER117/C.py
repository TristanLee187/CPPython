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
    k,x=rns()
    def f(steps):
        ans=0
        if steps<=k:
            ans+=steps*(steps+1)//2
        else:
            ans+=k*(k+1)//2
            left=max(0,2*k-steps-1)
            ans+=k*(k-1)//2 - left*(left+1)//2
        return ans
    lo=1
    hi=2*k
    ans=-1
    while lo<=hi:
        mid = (lo+hi)//2
        poss=f(mid-1)
        if poss<x:
            ans=max(ans,mid)
            lo=mid+1
        elif poss==x:
            ans=max(ans, mid-1)
            lo=mid+1
        else:
            hi=mid-1
        # print(mid, poss)
    print(min(ans, 2*k-1))
