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
    n=rn()
    a=rl()
    h=1
    for i in range(n):
        if a[i]==1:
            if i>0 and a[i-1]==1:
                h+=5
            else:
                h+=1
        else:
            if i>0 and a[i-1]==0:
                h=-1
                break
    print(h)