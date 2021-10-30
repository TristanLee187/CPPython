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
    n=rn()
    a=rl()
    ans=True
    f=[2]
    for i in range(n):
        found=False
        for num in f:
            if a[i]%num!=0:
                found=True
                break
        if not found:
            ans=False
            break
        f.append(i+3)
    YN(ans)
