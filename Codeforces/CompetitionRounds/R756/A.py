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
    n=rs()
    a=[int(i) for i in n]
    i=-1
    for j in range(len(n)):
        if a[j]%2==0:
            i=j
            break
    if i==-1:
        print(-1)
    elif a[-1]%2==0:
        print(0)
    elif i==0:
        print(1)
    else:
        print(2)