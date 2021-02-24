rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    m,h=rns()
    bmi=m/(h**2)
    if bmi<=18:
        print(1)
    elif bmi<=24:
        print(2)
    elif bmi<=29:
        print(3)
    else:
        print(4)
