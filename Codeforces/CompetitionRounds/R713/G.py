from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

m=int(1e7)+1
sieve=m*[1]
ans=m*[-1]
ans[1]=1
i=2
while i<m:
    j=i
    while j<m:
        sieve[j]+=i
        if sieve[j]>=m:
            break
        j+=i
    if sieve[i]<m and ans[sieve[i]]==-1:
        ans[sieve[i]]=i
    i+=1

for _ in range(rn()):
    print(ans[rn()])