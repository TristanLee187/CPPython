from sys import stdin
input=stdin.readline
rn=lambda:int(input())
rns=lambda:map(int,input().split())
rl=lambda:list(map(int,input().split()))
rs=lambda:input().strip()
YN=lambda x:print('YES') if x else print('NO')
mod=10**9+7

for _ in range(rn()):
    k=rn()
    r=int(k**0.5)
    if r**2==k:
        print(r,1)
    else:
        if r**2+r+1>k:
            print(k-r**2, r+1)
        else:
            print(r+1, (r+1)**2-k+1)
