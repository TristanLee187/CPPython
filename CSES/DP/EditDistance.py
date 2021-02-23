a=input()
b=input()
if a==b:
    print(0)
else:
    n=len(a)
    m=len(b)
    dp=[(m+1)*[5000] for i in range(n+1)]
    dp[0][0]=0
    for i in range(n+1):
        for j in range(m+1):
            if i>0:
                dp[i][j]=min(dp[i][j],dp[i-1][j]+1)
            if j>0:
                dp[i][j]=min(dp[i][j],dp[i][j-1]+1)
            if i>0 and j>0:
                dp[i][j]=min(dp[i][j],dp[i-1][j-1]+int(a[i-1]!=b[j-1]))
    print(dp[-1][-1])