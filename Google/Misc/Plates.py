rn = lambda: int(input())
rns = lambda: map(int, input().split())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
yn = lambda x: print('Yes') if x else print('No')
YN = lambda x: print('YES') if x else print('NO')
mod = lambda x: x % (10 ** 9 + 7)
from itertools import accumulate
for _ in range(rn()):
    n,k,p=rns()
    l=[]
    for i in range(n):
        a=rl()
        l.append([0]+list(accumulate(a)))
    dp=[]
    for i in range(n+1):
        dp.append((p+1)*[0])
    for i in range(1,n+1):
        for j in range(1,p+1):
            if i==1:
                if j<=k:
                    dp[i][j]=l[i-1][j]
            else:
                for v in range(min(j,k)+1):
                    dp[i][j]=max(dp[i][j],l[i-1][v]+dp[i-1][j-v])
    ans=dp[-1][-1]
    print('Case #' + str(_ + 1) + ': ' + str(ans))