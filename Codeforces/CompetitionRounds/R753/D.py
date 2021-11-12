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
    colors=rs()
    b=[a[i] for i in range(n) if colors[i]=='B']
    r=[a[i] for i in range(n) if colors[i]=='R']
    b.sort()
    r.sort()
    ans = all([b[i]>=i+1 for i in range(len(b))])
    ans = ans and all([r[i]<=i+1+len(b) for i in range(len(r))])
    YN(ans)