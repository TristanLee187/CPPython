from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,m,x=rns()
    a=rl()
    s=[[a[i],i] for i in range(n)]
    s.sort()
    ans=n*[0]
    for i in range(n):
        ans[s[i][1]]=(i%m)+1
    print('YES')
    print(*ans)
