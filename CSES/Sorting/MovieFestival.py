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
p=[]
for i in range(n):
    p.append(rl()[::-1])
p.sort()
ans=1
last=p[0][0]
for i in range(1,n):
    if p[i][1]>=last:
        ans+=1
        last=p[i][0]
print(ans)