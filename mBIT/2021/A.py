from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n=rn()
a=rl()
ans=n+a[0]
for i in range(1,n):
    ans+=abs(a[i]-a[i-1])
ans+=a[-1]
print(ans)
