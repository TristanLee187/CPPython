rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')
pl=lambda l:print(' '.join(list(map(str,l))))

for _ in range(rn()):
    r=rn()
    R=rl()
    b=rn()
    B=rl()
    pre1=[0]
    pre2=[0]
    for i in range(r):
        pre1.append(pre1[-1]+R[i])
    for i in range(b):
        pre2.append(pre2[-1]+B[i])
    print(max(pre1)+max(pre2))