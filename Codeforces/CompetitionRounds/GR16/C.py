from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rs()
    b=rs()
    seen=[False for i in range(n)]
    ans=0
    for i in range(n):
        if a[i]!=b[i]:
            seen[i]=True
            ans+=2

    for i in range(n-1):
        if a[i]==b[i] and a[i+1]==b[i+1] and a[i]!=a[i+1] and not seen[i+1] and not seen[i]:
            seen[i]=True
            seen[i+1]=True
            ans+=2

    for i in range(n):
        if a[i]==b[i]=='0' and not seen[i]:
            seen[i]=True
            ans+=1

    print(ans)
