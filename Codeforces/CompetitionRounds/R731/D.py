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
    ans=[0]
    for i in range(1,n):
        add=a[i-1] - (a[i] & a[i-1])
        ans.append(add)
        a[i]+=add

    print(*ans)
