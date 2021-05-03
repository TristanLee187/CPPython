from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,x=rns()
    w=rl()
    w.sort()
    ans=sum(w)!=x
    pre=0
    for i in range(n):
        pre+=w[i]
        if pre==x:
            if i==n-1:
                w[i],w[0] = w[0],w[i]
            else:
                w[i],w[-1] = w[-1],w[i]
            break
    YN(ans)
    if ans:
        print(*w)