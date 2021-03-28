rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    x,y=rns()
    x=abs(x)
    y=abs(y)
    ans=2*min(x,y)+(max((abs(x-y))*2-1,0))
    print(ans)
