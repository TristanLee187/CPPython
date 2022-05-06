from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

a=[]
m=4*10**4
for i in range(1,m+1):
    if str(i)==str(i)[::-1]:
        a.append(i)
c=len(a)
# Partition problem: make all numbers from 1 to n by summing palindromes
dp=[[0 for j in range(c)] for i in range(m+1)]
dp[0]=c*[1]
ans=[]
for i in range(m+1):
    for j in range(c):
        if j==0:
            dp[i][j]=1
        elif a[j]<=i:
            dp[i][j]=(dp[i][j-1] + dp[i-a[j]][j])%mod
        else:
            dp[i][j]=dp[i][j-1]

for _ in range(rn()):
    n=rn()
    print(dp[n][-1])
