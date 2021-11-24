from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    a,b,x=rns()
    if a>b:
        a,b=b,a
    ans=x in [a,b]
    while a!=0 and a<b and not ans and b>=x:
        if (b-x)%a==0:
            ans=True
            # print(x,a,b)
            break
        a,b=b%a,a
        # print(a,b)
    YN(ans)