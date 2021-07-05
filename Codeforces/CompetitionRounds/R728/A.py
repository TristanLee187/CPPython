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
    ans = list(range(1,n+1))
    for i in range(0, n-1, 2):
        ans[i], ans[i+1] = ans[i+1], ans[i]
    if n%2==1:
        ans[-1], ans[-2] = ans[-2],ans[-1]
    print(*ans)