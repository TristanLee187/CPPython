rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    l=rl()
    a=sum(l[::2])
    b=sum(l[1::2])
    if a<b:
        for i in range(0,n,2):
            l[i]=1
    else:
        for i in range(1,n,2):
            l[i]=1
    print(*l)
