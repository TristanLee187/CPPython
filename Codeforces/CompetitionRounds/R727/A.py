from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,x,t=rns()
    low=min(t//x+1,n)
    sumc = lambda x:x*(x+1)//2
    ans=max(sumc(n-1)-sumc(low-1),0)
    ans+=low*n
    ans-=sumc(n)
    print(ans)