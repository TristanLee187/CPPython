rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n,m=rns()
    l=rl()
    if m==0:
        YN(sum(l)==0)
    else:
        YN(sum(l)%m==0)
