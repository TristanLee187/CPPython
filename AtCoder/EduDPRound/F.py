rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))

s=rs()
t=rs()
dp=[]
for i in range(len(t)):
    dp.append(len(s)*[0])
for i in range(len(t)):
    for j in range(len(s)):
        if i==0:
            if j==0:
                dp[i][j]=int(t[i]==s[j])
            else:
                dp[i][j]=max(dp[i][j-1],int(t[i]==s[j]))
        elif j==0:
            dp[i][j] = max(dp[i-1][j], int(t[i] == s[j]))
        else:
            if t[i]==s[j]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
ans=""
i=len(t)
j=len(s)
while True:
    if t[i-1]==s[j-1]:
        ans+=s[j-1]
        i-=1
        j-=1
    elif