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
    h=rl()
    lo=min(h)
    hi=max(h)
    ans=lo
    def f(val, arr):
        for i in range(len(arr)-1,1,-1):
            if arr[i]<val:
                return False
            diff=min(arr[i]-val,h[i])
            diff-=diff%3
            arr[i]-=diff
            arr[i-1]+=diff//3
            arr[i-2]+=2*diff//3
        return arr[0]>=val and arr[1]>=val
    while lo<=hi:
        mid=(lo+hi)//2
        if f(mid,h.copy()):
            ans=max(ans,mid)
            lo=mid+1
        else:
            hi=mid-1
    print(ans)