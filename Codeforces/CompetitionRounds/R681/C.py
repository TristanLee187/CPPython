rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    a=rl()
    b=rl()
    l=[[a[i],b[i]] for i in range(n)]
    l.sort()
    pre=[0]
    for i in range(n-1,-1,-1):
        pre.append(pre[-1]+l[i][1])
    pre.pop(0)
    pre=pre[::-1]
    ans=l[-1][0]
    for i in range(n-1):
        ans=min(max(l[i][0],pre[i+1]),ans)
    print(min(ans,pre[0]))