rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)
def d(a):
    d={}
    for i in a:
        if i not in d:
            d[i]=0
        d[i]+=1
    return d

for _ in range(rn()):
    n,m=rns()
    a=rl()
    b=rl()
    dp=2*(n+1)*[0]
    for i in range(n):
        for j in range(len(dp),-1,-1):
            if j+b[i]<len(dp):
                dp[j+b[i]]=max(dp[j+b[i]],dp[j]+a[i])
    ans=-1
    for i in range(len(dp)):
        if dp[i]>=m:
            ans=i
            break
    print(ans)