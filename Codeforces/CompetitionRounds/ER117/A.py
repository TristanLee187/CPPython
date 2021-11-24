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
    x,y=rns()
    if (x+y)%2==1:
        print(-1,-1)
    elif x%2==0:
        print(x//2,y//2)
    else:
        if x>y:
            print((x+y)//2, 0)
        else:
            print(0, (x + y) // 2)