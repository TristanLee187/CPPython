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
    a=sorted([(a[i],i) for i in range(n)], reverse=True)
    # print(a)
    ans=[0 for i in range(n+1)]
    pans=0
    for i in range(n):
        if i%2==0:
            ans[a[i][1]+1]=(i//2+1)
        else:
            ans[a[i][1]+1]=(-(i//2+1))
        pans+=a[i][0]*(i//2+1)
    print(2*pans)
    print(*ans)
