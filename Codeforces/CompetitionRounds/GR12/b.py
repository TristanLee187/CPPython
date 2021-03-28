rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n,k=rns()
    points=[]
    ans=-1
    for i in range(n):
        points.append(rl())
    for i in range(n):
        b=[]
        for j in range(n):
            if i!=j:
                b.append(abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]))
        if all([i<=k for i in b]):
            ans=1
            break
    print(ans)