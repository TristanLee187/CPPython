rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n,m=rns()
    l=[]
    for i in range(n):
        l.append(rl())
    ans=0
    count=1
    m=float('inf')
    for i in l:
        for j in i:
            ans+=abs(j)
            m=min(m,abs(j))
            if j<0:
                count*=-1
    if count==-1:
        ans-=2*m
    print(ans)
