rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    n=rn()
    for i in range(n):
        if i==n-1:
            a=[1]
            for j in range(1,n-1):
                a.append(0)
            a.append(1)
            print(*a)
        else:
            a=i*[0]+[1,1]+(n-i-2)*[0]
            print(*a)