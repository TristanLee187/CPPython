from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,k=rns()
    a=rl()
    b=[]
    for i in range(n-1):
        b.append(10**(a[i+1]-a[i])-1)
    ans=0
    while len(b)>0 and k>=b[0]:
        ans+=b[0]*10**a[0]
        k-=b.pop(0)
        a.pop(0)

    if k>=0:
        if len(b)==0:
            last=a.pop(0)
            ans+=(k+1)*10**last
        else:
            ans+=(k+1)*10**a.pop(0)
    print(ans)