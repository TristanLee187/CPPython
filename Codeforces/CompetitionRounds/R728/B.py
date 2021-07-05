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
    a=rl()
    a = [(a[i], i+1) for i in range(n)]
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i][0] * a[j][0] > 2*n:
                break
            if a[i][0] * a[j][0] == a[i][1]+a[j][1]:
                ans+=1
    print(ans)