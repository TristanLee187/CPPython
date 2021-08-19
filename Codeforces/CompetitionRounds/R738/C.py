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
    if a[-1]==0:
        print(*list(range(1,n+2)))
    elif a[0]==1:
        print(*([n+1] + list(range(1,n+1))))
    elif sum(a) == n:
        print(-1)
    else:
        ans=list(range(1,n+1))
        for i in range(1,n):
            if a[i] and not a[i-1]:
                ans.insert(i,n+1)
                break
        print(*ans)