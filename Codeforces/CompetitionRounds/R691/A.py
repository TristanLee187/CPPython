rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    s1=rs()
    s2=rs()
    r=0
    b=0
    for i in range(n):
        if int(s1[i])>int(s2[i]):
            r+=1
        elif int(s1[i])<int(s2[i]):
            b+=1
    if r>b:
        print('RED')
    elif r<b:
        print('BLUE')
    else:
        print('EQUAL')