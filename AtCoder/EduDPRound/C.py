rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))

n=rn()
l=[]
for i in range(n):
    l.append(rl())
dp=[]
for i in range(n):
    dp.append(l[0].copy())
for i in range(1,n):
    for j in range(3):
        a=dp[i-1][(j+1)%3]
        b=dp[i-1][(j+2)%3]
        dp[i][j]=max(a,b)+l[i][j]
print(max(dp[-1]))