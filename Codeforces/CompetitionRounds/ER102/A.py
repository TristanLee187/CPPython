rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n,d=rns()
    l=rl()
    b=max(l)<=d
    i=l.index(min(l))
    a=min(l)
    l.pop(i)
    j=l.index(min(l))
    YN(a+l[j]<=d or b)