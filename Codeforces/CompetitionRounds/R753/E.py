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
    n,m=rns()
    s=rs()
    lr=[0,0]
    ud=[0,0]
    currx=0
    curry=0
    for i in s:
        if i=='R':
            currx+=1
            lr[1] = max(lr[1], currx)
        elif i=='L':
            currx-=1
            lr[0] = min(lr[0], currx)
        elif i=='U':
            curry+=1
            ud[0] = min(ud[0], curry)
        else:
            curry-=1
            ud[1] = max(ud[1], curry)
            ud[0] = min(ud[0], curry)
