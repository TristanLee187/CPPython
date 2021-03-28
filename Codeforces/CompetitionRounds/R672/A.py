rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    l=rl()
    ans=False
    for i in range(1,n):
        if l[i]>=l[i-1]:
            ans=True
            break
    yn(ans)