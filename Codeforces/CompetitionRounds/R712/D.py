rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n=rn()
ones = []
twos = []
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i+j)%2==0:
            ones.append((i,j))
        else:
            twos.append((i,j))

for _ in range(n**2):
    a=rn()
    if a!=1 and len(ones)>0:
        pos=ones.pop()
        print(1,*pos)
    elif a!=1 and len(ones)==0:
        pos=twos.pop()
        if a==2:
            print(3,*pos)
        else:
            print(2,*pos)
    elif a==1 and len(twos)>0:
        pos=twos.pop()
        print(2,*pos)
    elif a==1 and len(twos)==0:
        pos = ones.pop()
        print(3,*pos)