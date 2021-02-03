rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

n,x=rns()
h=rl()
s=rl()
dp=(10**5+1)*[-1]
dp[0]=0
for i in range(10**5+1):
    if dp[0]>-1:
        for j in range(n):
            if i+h[j]<10**5+1:
                dp[i+h[j]]=max(dp[i+h[j]],dp[i]+s[j])
print(dp[x])