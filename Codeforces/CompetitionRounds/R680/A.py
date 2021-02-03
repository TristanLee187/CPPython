rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

t=rn()
for _ in range(t):
    n,x=rns()
    a=rl()
    b=rl()
    if _<t-1:
        blank=input()
    a.sort()
    b.sort(reverse=True)
    ans=True
    for i in range(n):
        if a[i]+b[i]>x:
            ans=False
            break
    yn(ans)
