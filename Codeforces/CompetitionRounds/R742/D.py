from sys import stdin
from bisect import insort
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    s,n=rns()
    ans=[s]
    def b(x):
        i=0
        while x%(10**i)==0:
            i+=1
        return x%(10**i)
    flag=False
    for j in range(n-1):
        if b(ans[-1]==ans[-1]):
            flag=True
        else:
            a=b(ans[-1])
            ans[-1]-=a
            insort(ans,a)
        if flag:
            k=0
            while ans[k]<=1:
                k+=1
            ans[k]-=1
            insort(ans,1)
    print(*ans)
