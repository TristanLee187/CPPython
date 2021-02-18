rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=lambda x:x%(10**9+7)
def d(a):
    d={}
    for i in a:
        if i not in d:
            d[i]=0
        d[i]+=1
    return d

for _ in range(rn()):
    n=rn()
    a=[]
    b=[]
    for i in range(n):
        j,k=rns()
        a.append(j)
        b.append(k)
    a.sort()
    b.sort()
    x=0
    if n%2==1:
        x=1
    else:
        x=a[n//2]-a[n//2-1]+1
    y=0
    if n % 2 == 1:
        y = 1
    else:
        y = b[n // 2] - b[n // 2 - 1] + 1
    print(x*y)