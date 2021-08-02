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
    a=list(map(int, rs()))
    b=list(map(int, rs()))
    ans=0
    for i in range(n):
        if b[i]:
            if not a[i]:
                ans+=1
            elif i>0 and a[i-1]:
                ans+=1
                a[i-1]=0
            elif i<n-1 and a[i+1]:
                ans+=1
                a[i+1]=0
    print(ans)
