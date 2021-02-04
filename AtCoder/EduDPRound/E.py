rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
pl=lambda l:print(' '.join(list(map(str,l))))

n,w=rns()
items=[]
for i in range(n):
    items.append(rl())
dp=[]
for i in range(n+1):
    dp.append(10001*[float('inf')])
dp[0][0]=0
ans=0
for i in range(1,n+1):
    for j in range(10001):
        