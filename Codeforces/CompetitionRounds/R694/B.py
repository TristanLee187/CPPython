rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n,x=rns()
    l=rl()
    a=l.copy()
    ans=sum(l)
    i=0
    while a[i]%x==0:
        ans+=l[i]
        a[i]=a[i]//x
        i+=1
        i%=n
    print(ans)