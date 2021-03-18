rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7
import heapq

for _ in range(rn()):
    n=rn()
    c=rl()
    ans=n*c[0]+n*c[1]
    curr=ans
    h=[]
    heapq.heappush(h,[-c[0],n])
    last=[-c[1],n]
    for i in range(2,n):
        poss=heapq.heappop(h)
        if c[i]>=-poss[0]:
            curr-=-poss[0]
            curr+=c[i]
            poss[1]-=1
            heapq.heappush(h,poss)
            if last[1]!=1:
                heapq.heappush(h,last)
            last=[-c[i],1]
        else:
            curr-=(poss[1]-1)*-poss[0]
            curr+=c[i]*(poss[1]-1)
            if last[1]!=1:
                heapq.heappush(h,last)
            last=[-c[i],poss[-1]-1]
        ans=min(ans,curr)
    print(ans)