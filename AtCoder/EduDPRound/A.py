rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))

n=rn()
l=rl()
dp = n*[float('inf')]
dp[0]=0
for i in range(n):
    if i+1<n:
        dp[i+1]=min(dp[i+1],dp[i]+abs(l[i+1]-l[i]))
    if i+2<n:
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(l[i + 2] - l[i]))
print(dp[-1])