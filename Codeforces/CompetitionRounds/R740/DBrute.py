from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n,m=rns()
pre=1
dp=[1]
for i in range(2,n+1):
    add=sum(dp)
    print(i,add)
    for j in range(2,i+1):
        add+=dp[i//j-1]
        add%=m
    dp.append(add)
print(dp)
