from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    a,b,c=rns()
    n=2*abs(a-b)
    if max([a,b,c])>n:
        print(-1)
    else:
        ans=c+n//2
        if ans>n:
            ans-=n
        print(ans)
