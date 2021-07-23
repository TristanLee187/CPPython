from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n, a, b = rns()
    s = rs()
    c=1
    for i in range(1,n):
        if s[i]!=s[i-1]:
            c+=1
    ans = max(n * a + n * b, n * a + (c//2+1) * b)
    print(ans)