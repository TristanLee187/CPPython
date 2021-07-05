from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,a,b=rns()
    if a==1:
        YN((n-1)%b==0 or n==1)
    else:
        root=a
        a=1
        ans = False
        while a<=n:
            ans = ans or (n-a)%b==0
            a*=root
        YN(ans or n==1)