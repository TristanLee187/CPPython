from sys import stdin
input = stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

a=[rn() for i in range(2000)]
b=[sum(a[i:i+3]) for i in range(1998)]

ans=0
for i in range(1,len(b)):
    if b[i]>b[i-1]:
        ans+=1
print(ans)