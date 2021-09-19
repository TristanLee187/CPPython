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
    s=rs()
    ans=0
    for i in range(n):
        ans+=int(s[i])
        if int(s[i]) and i!=n-1:
            ans+=1
    print(ans)