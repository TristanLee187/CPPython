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
x=sum([i[1] for i in items])
dp=(x+1)*[float('inf')]
dp[0]=0
for i in range(n):
    weight=items[i][0]
    val=items[i][1]
    for j in range(x-val,-1,-1):
        dp[j+val]=min(dp[j+val],dp[j]+weight)
for i in range(x,-1,-1):
    if dp[i]<=w:
        print(i)
        break