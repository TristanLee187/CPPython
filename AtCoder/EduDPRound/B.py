rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))

n,k=rns()
l=rl()
dp = n*[float('inf')]
dp[0]=0
for i in range(n):
    for j in range(1,k+1):
        if i+j<n:
            dp[i+j]=min(dp[i+j],dp[i]+abs(l[i+j]-l[i]))

print(dp[-1])