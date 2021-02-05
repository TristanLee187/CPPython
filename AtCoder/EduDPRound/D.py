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
dp=(w+1)*[0]
for i in range(n):
    weight=items[i][0]
    val=items[i][1]
    for j in range(w-weight,-1,-1):
        dp[j+weight]=max(dp[j+weight],dp[j]+val)
print(max(dp))