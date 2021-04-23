from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    if n%2050==0:
        a=n//2050
        ans=0
        for i in str(a):
            ans+=int(i)
        print(ans)
    else:
        print(-1)