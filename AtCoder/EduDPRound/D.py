rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))

n,w=rns()
items=[]
for i in range(n):
    items.append(rl())
dp=[]
for i in range(n+1):
    dp.append((w+1)*[0])

for i in range(1,n+1):
    for j in range(w+1):
        dp[i][j]=dp[i-1][j]
        if j-items[i-1][0]>=0:
            dp[i][j]=max(dp[i][j],dp[i-1][j-items[i-1][0]]+items[i-1][1])
print(dp[-1][-1])