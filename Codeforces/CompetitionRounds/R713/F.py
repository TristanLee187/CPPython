rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
from math import ceil

for _ in range(rn()):
    n,c=rns()
    a=rl()
    b=rl()
    b.insert(0,0)

    dp=n*[0]
    time=n*[0]
    rem=n*[0]

    dp[0] = ceil(c/a[0])
    for i in range(1,n):
        time[i]=time[i-1]+ceil((b[i]-rem[i-1])/a[i-1])+1
        rem[i]=a[i-1]-((b[i]-rem[i-1])%a[i-1])
        if rem[i]==a[i-1]:
            rem[i]=0
        poss=ceil((c-rem[i])/a[i])+time[i]
        dp[i] = min(dp[i-1], poss)
    print(dp[-1])