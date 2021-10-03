from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,h=rns()
    a=sorted(rl())
    b,c=a[-1],a[-2]
    ans=2*(h//(b+c))
    h=h%(b+c)
    while h>0:
        h-=b
        b,c=c,b
        ans+=1
    print(ans)