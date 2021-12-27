from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
ceil_div=lambda a,b:-(-a//b)
mod=10**9+7

for _ in range(rn()):
    a=rl()
    ans=False
    for i in range(3):
        others=[a[j] for j in range(3) if j!=i]
        if sum(others)==a[i] or (len(set(others))==1 and a[i]%2==0):
            ans=True
    YN(ans)