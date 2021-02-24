rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rl()
    p=[]
    for i in range(n):
        p.append([a[i],i])
    p.sort(key=lambda x:[n-x[0],x[1]])
    ans=n*[-1]
    for i in range(n):
        ans[p[i][1]]=i+1
    print(*ans)