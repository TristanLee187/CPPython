from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    n,k=rns()
    a=rl()
    b=sorted(a)
    d={}
    for i in range(n):
        d[b[i]]=i
    c=1
    for i in range(1,n):
        if d[a[i]]!=d[a[i-1]]+1:
            c+=1
    YN(c<=k)