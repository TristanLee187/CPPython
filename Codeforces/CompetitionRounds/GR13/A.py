rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

n,q=rns()
a=rl()
b=sorted(a)
i=0
if b[-1]==1:
    i=n-b.index(1)
for j in range(q):
    c,d=rns()
    if c==2:
        if d<=i:
            print(1)
        else:
            print(0)
    else:
        if a[d-1]==1:
            i-=1
            a[d-1]=0
        else:
            i+=1
            a[d-1]=1
