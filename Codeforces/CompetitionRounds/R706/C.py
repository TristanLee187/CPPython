rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    mine=[]
    miner=[]
    for i in range(2*n):
        x,y=rns()
        if x==0:
            miner.append(y)
        else:
            mine.append(x)
    mine=sorted(list(map(abs,mine)))
    miner=sorted(list(map(abs,miner)))
    ans=0
    for i in range(n):
        ans+=(mine[i]**2+miner[i]**2)**0.5
    print(ans)