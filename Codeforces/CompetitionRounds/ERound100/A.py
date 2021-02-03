rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    a,b,c=rns()
    ans=(a+b+c)%9==0 and (a+b+c)//9<=min([a,b,c])
    YN(ans)