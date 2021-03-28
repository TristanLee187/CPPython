rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

for _ in range(rn()):
    n,k=rns()
    l=rl()
    l.sort()
    ans=l[-1]-l[0]
    a=True
    for i in range(k):
        if a:
            a=False
            ans+=l[0]
        ans+=l[-2-i]
    print(ans)