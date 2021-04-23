from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n,m,k=rns()
rows=[rl() for i in range(n)]
cols=[rl() for i in range(n-1)]
def solve():
    if k%2==1:
        return [m*[-1] for i in range(n)]
    dp=[[[0 for i in range(k//2+1)] for j in range(m)] for l in range(n)]
    for i in range(1,k//2+1):
        for a in range(n):
            for b in range(m):
                mins=[]
                if b>0:
                    mins.append(dp[a][b-1][i-1] + 2*rows[a][b-1])
                if b<m-1:
                    mins.append(dp[a][b + 1][i - 1] + 2 * rows[a][b])
                if a>0:
                    mins.append(dp[a-1][b][i - 1] + 2 * cols[a-1][b])
                if a<n-1:
                    mins.append(dp[a+1][b][i - 1] + 2 * cols[a][b])
                dp[a][b][i]=min(mins)
    ans=[[dp[i][j][-1] for j in range(m)] for i in range(n)]
    return ans

ans = solve()
for i in ans:
    print(*i)