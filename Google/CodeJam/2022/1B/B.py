from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    ans=0
    n,p=rns()
    a=[rl() for _ in range(n)]
    for i in range(n):
        m,mi=max(a[i]), min(a[i])
        if i==0:
            ans+=m
        else:
            ans+=m-mi
        a[i]=[mi,m]
    dp=[[0,a[0][1]-a[0][0]] for i in range(n)]
    for i in range(1,n):
        dp[i][0] = min(dp[i-1][0] + abs(a[i][0] - a[i-1][1]), dp[i-1][1] + abs(a[i][0] - a[i-1][0]))
        dp[i][1] = min(dp[i - 1][0] + abs(a[i][1] - a[i - 1][1]), dp[i - 1][1] + abs(a[i][1] - a[i - 1][0]))
    ans += min(dp[-1])
    # print(dp)
    print('Case #' + str(_+1)+': ' + str(ans))