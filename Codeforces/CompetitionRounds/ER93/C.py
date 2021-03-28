for _ in range(int(input())):
    n=int(input())
    s=input()
    dp =[0]*(9*n)
    dp[0]=1
    a=0
    ans=0
    for i in range(n):
        a+=int(s[i])
        ans+=dp[a-i-1]
        dp[a-i-1]+=1
    print(ans)
