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
    b=sorted(a)
    ans=0
    while a!=b:
        ans+=1
        for i in range(not (ans%2), n-ans%2):
            if i%2!=ans%2:
                a[i],a[i+1] = sorted([a[i+1],a[i]])
    print(ans)