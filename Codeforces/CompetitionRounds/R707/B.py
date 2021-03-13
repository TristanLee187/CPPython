rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n=rn()
    a=rl()
    a.reverse()
    c=[a[0]]
    for i in range(1,n):
        c.append(max(c[-1]-1,a[i]))
    ans=[1 if c[i]>0 else 0 for i in range(n)]
    print(*reversed(ans))