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
    ans=0
    m=-1
    ma=max(a)
    while a:
        if a[-1]==ma:
            break
        if a[-1]>m:
            ans+=1
            m=a[-1]
        a.pop()
    print(ans)