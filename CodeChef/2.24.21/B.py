rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,k=rns()
    a=rl()
    p=[]
    for i in range(n):
        p.append(rs())
    ans=[]
    for i in range(n):
        acc=0
        for j in range(k):
            if p[i][j]=='1':
                acc+=a[j]
        ans.append(acc)
    for i in ans:
        print(i)