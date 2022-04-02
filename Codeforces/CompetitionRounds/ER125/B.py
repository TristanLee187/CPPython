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
    n,b,x,y=rns()
    a=[0]
    for i in range(n):
        if a[-1]+x>b:
            a.append(a[-1]-y)
        else:
            a.append(a[-1]+x)
    print(sum(a))