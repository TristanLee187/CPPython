from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n=rn()
a=rl()
dp=[(n+1)*[-float('inf')] for i in range(n)]
for i in range(n):
    if i==0:
        dp[0][0]=0
        dp[0][1]=a[i]
    else:
        for j in range(i+2):
            if j==0:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j] = dp[i - 1][j]
                dp[i][j]=max(dp[i][j],dp[i-1][j-1]+a[i])
                if dp[i][j]<0:
                    dp[i][j]=-float('inf')
ans=0
for i in range(len(dp[-1])):
    if dp[-1][i]>=0:
        ans=max(ans,i)
print(ans)
