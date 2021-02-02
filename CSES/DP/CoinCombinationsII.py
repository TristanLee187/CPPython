n,x=map(int,input().split())
l=list(map(int,input().split()))
dp=[]
for i in range(n+1):
    dp.append((x+1)*[0])
dp[0][0]=1
for i in range(n):
    for j in range(x+1):
        if j==0:
            dp[i+1][j]=1
        else:
            dp[i+1][j] = dp[i][j]
            if j>=l[i]:
                dp[i+1][j]+=dp[i+1][j-l[i]]
            dp[i+1][j] %= (10**9+7)
print(dp[-1][-1])