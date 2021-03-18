rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    c=rl()
    ans=n*(c[0]+c[1])
    lengths=[n,n]
    curr=ans
    ru=[0,1]
    for i in range(2,n):
        if c[i]>=c[ru[i%2]]:
            curr-=c[ru[i%2]]
            curr+=c[i]
            lengths[ru[i%2]]-=1
            lengths.append(1)
        else:
            curr-=c[ru[i%2]]*(lengths[ru[i%2]]-1)
            curr+=c[i]*(lengths[ru[i%2]]-1)
            lengths.append(lengths[ru[i%2]]-1)
            lengths[ru[i % 2]]-=1
            ru[i%2]=i
        ans=min(ans,curr)
    print(ans)