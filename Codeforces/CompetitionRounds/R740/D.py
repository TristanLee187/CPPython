from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n,m=rns()

sieve=[[1,i] for i in range(n+1)]
for i in range(2,n+1):
    if len(sieve[i])==2:
        for j in range(2*i,n+1,i):
            sieve[j].append(i)
            if j//i != i:
                sieve[j].append(j//i)
for i in range(2,n+1):
    sieve[i].sort()
print(sieve)

pre=1
dp=[1]
for i in range(2,n+1):
    add=pre
    p=0
    div=sieve[i][p]
    while p<len(sieve[i])-1:
        add+=(i//div - i//(div+1)) * dp[div-1]
        add%=m
        p+=1
        div=sieve[i][p]
    add%=m
    dp.append(add)
    pre+=add
    pre%=m
print(dp)
